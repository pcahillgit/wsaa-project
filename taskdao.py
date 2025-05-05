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

taskDAO = TaskDAO()