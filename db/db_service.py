import json
import sqlite3
def init_database():
    conn = sqlite3.connect('users.db')
    sql = '''CREATE TABLE users (
            user_id TEXT PRIMARY KEY,
            state INT,
            color TEXT,
            storage TEXT);'''
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.close()

def add_user(user_id):
    try:
        get_user_state(user_id)
    except:
        conn = sqlite3.connect('./db/users.db')
        sql = "INSERT INTO `users` (user_id, state, color, storage) VALUES (?, ?, ?, ?)"
        values = (user_id, 0, json.dumps(((0,0,0),(255,255,255))), "None")
        cursor = conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        conn.close()

def update_user_state(user_id, state):
    conn = sqlite3.connect('./db/users.db')
    sql = "UPDATE users SET state = ? WHERE user_id = ?"
    cursor = conn.cursor()
    cursor.execute(sql, (state, user_id))
    conn.commit()
    conn.close()

def update_user_storage(user_id, storage):
    conn = sqlite3.connect('./db/users.db')
    sql = "UPDATE users SET storage = ? WHERE user_id = ?"
    cursor = conn.cursor()
    cursor.execute(sql, (json.dumps(storage), user_id))
    conn.commit()
    conn.close()

def update_user_color(user_id, color):
    conn = sqlite3.connect('./db/users.db')
    sql = "UPDATE users SET color = ? WHERE user_id = ?"
    cursor = conn.cursor()
    cursor.execute(sql, (json.dumps(color), user_id))
    conn.commit()
    conn.close()

def get_user_state(user_id):
    conn = sqlite3.connect('./db/users.db')
    sql = "SELECT state FROM users WHERE user_id = ?"
    cursor = conn.cursor()
    cursor.execute(sql, (user_id,))
    state = cursor.fetchone()[0]
    conn.close()
    return state

def get_user_storage(user_id):
    conn = sqlite3.connect('./db/users.db')
    sql = "SELECT storage FROM users WHERE user_id = ?"
    cursor = conn.cursor()
    cursor.execute(sql, (user_id,))
    storage = cursor.fetchone()[0]
    conn.close()
    return json.loads(storage)

def get_user_color(user_id):
    conn = sqlite3.connect('./db/users.db')
    sql = "SELECT color FROM users WHERE user_id = ?"
    cursor = conn.cursor()
    cursor.execute(sql, (user_id,))
    color = cursor.fetchone()[0]
    conn.close()
    return json.loads(color)

if __name__ == "__main__":
    init_database()