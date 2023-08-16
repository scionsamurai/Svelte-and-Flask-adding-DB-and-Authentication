import psycopg2
from werkzeug.security import generate_password_hash, check_password_hash

from db.hide import variables

def get_db_connection():
    conn = psycopg2.connect(
        dbname=variables.your_database_name,
        user=variables.your_username,
        password=variables.your_password,
        host=variables.your_host,
        port=variables.your_port
    )
    return conn
    
class User:
    name = ""
    password = ""

    def __init__(self, name="", password=""):
        self.name = name
        self.password = password
        self.id = 0

    def is_authenticated(self):
        query = 'SELECT * FROM "User" WHERE username = %s;'
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(query, (self.name,))
        data = cur.fetchone()
        print('data', data)
        cur.close()
        conn.close()
        if data is None:
            return False
        else:
            print("self.check_password(data[1])", self.check_password(data[1]))
            if self.check_password(data[1]):
                return True
            else:
                return False

    def is_active(self):
        return True

    def get_id(self):
        return str(self.name)

    def set_password(self, passwordy):
        self.pw_hash = passwordy
        # self.pw_hash = generate_password_hash(passwordy)

    def check_password(self, passwordx):
        return passwordx == self.password
        # return check_password_hash(passwordx, self.password)

    @staticmethod
    def get(user_name):
        query = 'SELECT * FROM "User" WHERE username = %s;'
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(query, (user_name,))
        data = cur.fetchone()
        user = User()
        if data:
            user.name = data[0]
            cur.close()
            conn.close()
            return user
        else:
            cur.close()
            conn.close()
            return None

