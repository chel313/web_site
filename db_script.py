# import sqlite3

# conn = None
# cursor = None
# def open_db():
#     global conn, cursor
#     conn = sqlite3.connect(db_name)
#     cursor = conn.cursor()

# def close():
#     cursor.close()
#     conn.close()

# def do(query):
#     cursor.execute(query)
#     conn.commit()

# def create():
#     do('''CREATE TABLE IF NOT EXISTS user(id PRIMARY KEY,name VARCHAR,)''') 
#     do('''CREATE TABLE IF NOT EXISTS questions(id PRIMARY KEY,question TEXT,true_answer TEXT,wrong_1 TEXT,
#     wrong_2 TEXT''')
#     do('''CREATE TABLE IF NOT EXISTS regions(id PRIMARY KEY,region VARCHAR)''')