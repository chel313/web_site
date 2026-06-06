from flask import Flask,redirect,request,session,render_template,url_for
from tables_scripts import get_question_after, check_answer
from random import randint, shuffle
import os 

quiz = 0
question_last = 0

def save_answers():
    answer = request.form.get('answer')
    quest_id = request.form.get('q_id')
    session['last_question'] = quest_id
    session['total'] += 1
    if check_answer(quest_id,answer):
        session['answers'] += 1


def quiz_form():
    quiz_id = request.form.get('quiz')
    return quiz_id

def question_form(question):
    answers_list = [question[2],question[3],question[4],question[5]]
    shuffle(answers_list)
    return render_template('test.html',question = question[1],quest_id = question[0],
                           answers_list = answers_list)

def index():
    global quiz,question_last
    quiz = randint(1,3)

    if request.method == 'GET':
        return render_template('index.html')  # Передаем в template
    
    if request.method == 'POST':
        quiz = quiz_form()
        if quiz is None:
            quiz = 1
        session['quiz'] = quiz
        session['last_question'] = 0
        session['total'] = 0
        session['answers'] = 0
        return redirect(url_for('test'))

def test():
    if not ('quiz' in session) or int(session['quiz']) < 0:
        return redirect(url_for('index'))
    if request.method == 'POST':
        save_answers()
    next_question = get_question_after(session['last_question'], session['quiz'])
    if next_question is None or len(next_question) == 0:
        return redirect(url_for('result'))
    else:
        return question_form(next_question)
    

def result():
    total = session.get('total',0)
    answers = session.get('answers',0)
    return render_template('result.html',answers=answers,total=total)

folder = os.getcwd()
app = Flask(__name__,template_folder='templates', static_folder='static') # создаём объект веб-приложения
app.add_url_rule('/', 'index', index,methods=['post', 'get'])   # создаёт правило для URL '/'
app.add_url_rule('/test', 'test', test,methods=['post', 'get']) # создаёт правило для URL '/test'
app.add_url_rule('/result', 'result', result) # создаёт правило для URL '/test'
app.config['SECRET_KEY'] = 'VeryStrongKey'

if __name__ == "__main__":
    app.run()  # запускаем веб-сервер