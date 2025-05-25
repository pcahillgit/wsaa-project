import sqlite3
import os

class TaskDAO:
    def __init__(self):
        self.dbfile = os.path.join(os.path.dirname(__file__), "tasks.db")
        self.init_db()

    def getConnection(self):
        return sqlite3.connect(self.dbfile)

    def init_db(self):
        with self.getConnection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS tasks (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    assigned_to TEXT,
                    done BOOLEAN
                )
            ''')
            conn.commit()

    def getAll(self):
        conn = self.getConnection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tasks")
        results = cursor.fetchall()
        conn.close()
        return [dict(id=row[0], title=row[1], assigned_to=row[2], done=bool(row[3])) for row in results]

    def findByID(self, id):
        conn = self.getConnection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tasks WHERE id = ?", (id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return dict(id=row[0], title=row[1], assigned_to=row[2], done=bool(row[3]))
        else:
            return {}

    def create(self, task):
        conn = self.getConnection()
        cursor = conn.cursor()
        sql = "INSERT INTO tasks (title, assigned_to, done) VALUES (?, ?, ?)"
        values = (task['title'], task['assigned_to'], task['done'])
        cursor.execute(sql, values)
        conn.commit()
        new_id = cursor.lastrowid
        conn.close()
        return new_id

    def update(self, id, task):
        conn = self.getConnection()
        cursor = conn.cursor()
        sql = "UPDATE tasks SET title = ?, assigned_to = ?, done = ? WHERE id = ?"
        values = (task['title'], task['assigned_to'], task['done'], id)
        cursor.execute(sql, values)
        conn.commit()
        conn.close()
        return True

    def delete(self, id):
        conn = self.getConnection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tasks WHERE id = ?", (id,))
        conn.commit()
        conn.close()
        return True

taskDAO = TaskDAO()