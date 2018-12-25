import data_base

class Users_data():
    def __init__(self):
        self.db = data_base.Data_Base()
        self.db.connect_to_data_base()
        self.connection = self.db.get_connection()
        self.cursor = self.db.db_cursor

    def get_users(self, username = '', email = ''):
        if username == '' and email == '':
            self.cursor.execute("select login, email, balance from users")
        else:
            if username == '': 
                self.cursor.execute("select login, email, balance from users where email = %s", (email))
            if email == '': 
                self.cursor.execute("select login, email, balance from users where login = %s", (username))
        return self.cursor.fetchall()

    def add_user(self, username = '', email = '', password = ''):
        if username == '' or email == '' or email == '':
            return 0
        else:
            self.connection.begin()
            self.cursor.execute("INSERT INTO users (login, password, email) VALUES (%s, %s, %s)", (username, password, email))
            self.connection.commit()
            return 1

    def alter_user(self, login, username = '', email = '', password = '', balance_change = 0):
        if username == '' and email == '' and email == '' and balance_change == 0:
            return 0
        else:
            self.connection.begin()
            if username != '':
                self.cursor.execute("UPDATE users SET login = %s WHERE login = %s;", (username, login))
            if password != '':
                self.cursor.execute("UPDATE users SET password = %s WHERE login = %s;", (password, login))
            if email != '':
                self.cursor.execute("UPDATE users SET email = %s WHERE login = %s;", (email, login))
            if balance_change != 0:
                self.cursor.execute("UPDATE users SET balance = balance + %s WHERE login = %s;", (balance_change, login))
            self.connection.commit()
        return 1

    def delete_user(self, username):
        if username == '':
            return 0
        else:
            self.connection.begin()
            self.cursor.execute("DELETE FROM users WHERE login = %s", (username))
            self.connection.commit()
        return 1

'''#uncoment to test
a = Users_data()
print(a.get_users())
print(a.add_user(username = '', email = '', password = ''))
print(a.add_user(username = 'q', email = 'q@q.q', password = 'q'))
print(a.get_users())
print(a.alter_user('q', username = 'q1'))
print(a.get_users())
print(a.delete_user('q1'))
print(a.get_users())
'''
