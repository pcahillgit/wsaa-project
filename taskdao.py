import mysql.connector

class TaskDAO:
    def __init__(self):
        self.host = "localhost"
        self.user = "root"
        self.password = ""
        self.database = "wsaa"

    def getConnection(self):
        return mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )

    def getAll(self):
        db = self.getConnection()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM tasks")
        results = cursor.fetchall()
        db.close()
        return results

    def findByID(self, id):
        db = self.getConnection()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM tasks WHERE id = %s", (id,))
        result = cursor.fetchone()
        db.close()
        return result

    def create(self, task):
        db = self.getConnection()
        cursor = db.cursor()
        sql = "INSERT INTO tasks (title, assigned_to, done) VALUES (%s, %s, %s)"
        values = (task['title'], task['assigned_to'], task['done'])
        cursor.execute(sql, values)
        db.commit()
        new_id = cursor.lastrowid
        db.close()
        return new_id

    def update(self, id, task):
        db = self.getConnection()
        cursor = db.cursor()
        sql = "UPDATE tasks SET title = %s, assigned_to = %s, done = %s WHERE id = %s"
        values = (task['title'], task['assigned_to'], task['done'], id)
        cursor.execute(sql, values)
        db.commit()
        db.close()
        return True

    def delete(self, id):
        db = self.getConnection()
        cursor = db.cursor()
        cursor.execute("DELETE FROM tasks WHERE id = %s", (id,))
        db.commit()
        db.close()
        return True

taskDAO = TaskDAO()