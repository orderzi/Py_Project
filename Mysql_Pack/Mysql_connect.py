import mysql.connector

class MysqlConnector:
    def __init__(self, **kwargs):
        self.username = kwargs['username']
        self.password = kwargs['password']
        self.database = kwargs['database']
        self.host = kwargs['host']
        self.connection = self._connect()

    def _connect(self):
        return mysql.connector.connect(
            host=self.host,
            user=self.username,
            password=self.password,
            database=self.database
        )

    def _create_cursor(self):
        return self.connection.cursor()

    def get_score(self, username):
        sql = f"SELECT scores from scores where username = %s"
        val = (username,)
        mycursor = self._create_cursor()
        mycursor.execute(sql, val)
        score = mycursor.fetchone()
        mycursor.close()
        if score == None:
            return 0
        else:
            return score[0]

    def set_score(self, username, scores):
        sql = f"INSERT INTO scores (username,scores) VALUES (%s, %s) ON DUPLICATE KEY UPDATE username=%s, scores=%s"
        score = self.get_score(username)
        scores += score
        val = (username, scores, username, scores)
        mycursor = self._create_cursor()
        mycursor.execute(sql, val)
        mycursor.close()
        self.connection.commit()