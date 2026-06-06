import sqlite3
db_name = 'quiz.sqlite'
conn = None
cursor = None

def open_db():
    global conn, cursor
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

def close():
    cursor.close()
    conn.close()

def do(query):
    cursor.execute(query)
    conn.commit()

def clear_db():
    ''' удаляет все таблицы '''
    open_db()
    query = '''DROP TABLE IF EXISTS quiz_content'''
    do(query)
    query = '''DROP TABLE IF EXISTS question'''
    do(query)
    query = '''DROP TABLE IF EXISTS quiz'''
    do(query)
    close()

    
def create():
    open_db()
    cursor.execute('''PRAGMA foreign_key=on''')

    do('''
    CREATE TABLE IF NOT EXISTS quiz (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR)
    ''')
    
    do('''
    CREATE TABLE IF NOT EXISTS question (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        question VARCHAR,
        answer VARCHAR,
        wrong1 VARCHAR,
        wrong2 VARCHAR,
        wrong3 VARCHAR
    )
    ''')
    
    do('''
    CREATE TABLE IF NOT EXISTS quiz_content (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        quiz_id INTEGER NOT NULL,
        question_id INTEGER NOT NULL,
        FOREIGN KEY (quiz_id) REFERENCES quiz (id) ON DELETE CASCADE,
        FOREIGN KEY (question_id) REFERENCES question (id) ON DELETE CASCADE
    )
    ''')
    
    close()

def add_questions():
    questions = [
        ("Сколько будет 2^2?", "4", "3", "5", "6"),
        ("Чему равно число Пи?", "примерно 3.14", "3", "3.1415", "3.1"),
        ("Кто написал 'Войну и мир'?", "Толстой", "Достоевский", "Пушкин", "Чехов"),
        ("В каком году началась Первая мировая война?", "1914", "1917", "1939", "1848"),
        ("Какая река самая длинная в мире?", "Нил", "Амазонка", "Волга", "Янцзы"),
        ("Какой океан самый большой?", "Тихий", "Атлантический", "Индийский", "Северный Ледовитый"),
        ("Сколько лет длилась Столетняя война?", "116", "100", "117", "99"),
        ("Чему равен синус 30 градусов?", "1/2", "1", "3/2", "0"),
        ("Самый маленький малонаселенный регион РФ?", "Ненецкий автономный округ", "Чукотский автономный округ", "Камчатский край", 
        "Еврейская автономная область"),
        ("Градусная мера угла квадрата ?", "90", "60", "180", "360"),
        ("В каком веке появилось книгопечатание?", "xv","xvi","xiv","xvii"),
        ("Сколько часовых поясов в России?","11","12","10","9")
    ]
    open_db()
    cursor.executemany("INSERT INTO question (question, answer, wrong1, wrong2, wrong3) VALUES (?,?,?,?,?)", questions)
    conn.commit()
    close()

def add_quiz():
    quizes = [
        ('Географический тест',),
        ('Мини тест на историю',),
        ('Мини тест на математику',)
    ]
    open_db()
    cursor.executemany('''INSERT INTO quiz (name) VALUES (?)''',quizes)
    conn.commit()
    close()

def add_links():
    open_db()
    cursor.execute('''PRAGMA foreign_keys=on''')
    query = "INSERT INTO quiz_content (quiz_id, question_id) VALUES (?,?)"
    answer = input("Добавить связь (y / n)? ")
    while answer != 'n':
        quiz_id = int(input("id викторины: "))
        question_id = int(input("id вопроса: "))
        cursor.execute(query, [quiz_id, question_id])
        conn.commit()
        answer = input("Добавить связь (y / n)? ")
    close()

def show(table):
    query = 'SELECT * FROM ' + table
    open_db()
    cursor.execute(query)
    print(cursor.fetchall())
    close()

def show_tables():
    show('question')
    show('quiz')
    show('quiz_content')

def get_question_after(question_id = 0, quiz_id=1):
    open_db()
    query = '''
        SELECT q.id, q.question, q.answer, q.wrong1, q.wrong2, q.wrong3
        FROM question q
        JOIN quiz_content qc ON q.id = qc.question_id
        WHERE qc.quiz_id = ? AND q.id > ?
        ORDER BY q.id ASC
        LIMIT 1
    '''
    cursor.execute(query, (quiz_id, question_id))
    result = cursor.fetchone()
    close()
    return result

def check_answer(quest_id,answer):
    query = ''' SELECT question.answer 
                FROM quiz_content,question
                WHERE quiz_content.id = ?
                AND quiz_content.question_id = question.id
            '''
    open_db()
    cursor.execute(query,int(quest_id,))
    result = cursor.fetchone()
    close()
    return result

def main():
    clear_db()
    create()
    add_questions()
    add_quiz()
    show_tables()
    
main()




