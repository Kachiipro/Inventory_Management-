import mysql.connector


class Database:

    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="123456",
            database="my_store"
        )
        self.cursor = self.conn.cursor()

    def execute_q(self, query, params=None):
        self.cursor.execute(query, params)
        self.conn.commit()

    def fetch_q(self, query, params=None):
        self.cursor.execute(query, params)
        return self.cursor.fetchall()

    def close_conn(self):
        self.cursor.close()
        self.conn.close()
