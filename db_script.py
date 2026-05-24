import sqlite3
from random import randint
db_name = 'test.sqlite'
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
    CREATE TABLE IF NOT EXISTS user (
        id INTEGER PRIMARY KEY,
        username NAME)
    ''')

    do('''
    CREATE TABLE IF NOT EXISTS regions(
        id INTEGER PRIMARY KEY,
        region TEXT)
    ''')

    do('''
    CREATE TABLE IF NOT EXISTS question (
        id INTEGER PRIMARY KEY,
        question TEXT,
        answer TEXT,
        wrong1 TEXT,
        wrong2 TEXT
    )
    ''')
    
    close()

def rendom_choice():
    open_db()
    regions = [

    ]
    cursor.execute('''PRAGMA foreing key=on''')
    cursor.executemant("INSERT INTO regions(id,region)"(regions))
    close()
