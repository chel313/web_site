from flask import Flask

def index():
    return ('Hello world')

app = Flask(__name__)
app.add_url_rule('/',index,'index')
if __name__ == '__main__':
    app.run()