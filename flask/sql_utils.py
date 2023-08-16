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

    def __init__(self, name="", password="", email=""):
        self.name = name
        self.password = password
        self.password_hash = generate_password_hash(password)
        self.email = email
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

    def check_password(self, passwordx):
        return check_password_hash(passwordx, self.password)

    def save_to_db(self):
        query = 'INSERT INTO "User" (username, password, email) VALUES (%s, %s, %s);'
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(query, (self.name, self.password_hash, self.email))  # Store the hashed password
        conn.commit()
        cur.close()
        conn.close()

    def is_valid(self, confirm_password):
        errors = []
        if not self.name or not self.email or not self.password:
            errors.append("All Fields are required to proceed.")

        if self.password != confirm_password:
            print(self.password, confirm_password)
            errors.append("Passwords do not match.")

        if self.check_duplicate_username():
            errors.append("Username is already being used.")

        if self.check_duplicate_email():
            errors.append("Email is already being used.")

        if len(self.password) < 8:
            errors.append("Password is not long enough.")

        if len(errors):
            return [False, errors]

        return [True,]

    def check_duplicate_username(self):
        query = 'SELECT COUNT(*) FROM "User" WHERE username = %s;'
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(query, (self.name,))
        count = cur.fetchone()[0]
        cur.close()
        conn.close()
        return count > 0

    def check_duplicate_email(self):
        query = 'SELECT COUNT(*) FROM "User" WHERE email = %s;'
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(query, (self.email,))
        count = cur.fetchone()[0]
        cur.close()
        conn.close()
        return count > 0

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
            user.email = data[2]  # Assuming email is stored at index 2 in the result
            cur.close()
            conn.close()
            return user
        else:
            cur.close()
            conn.close()
            return None
            
