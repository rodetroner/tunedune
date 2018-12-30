import data_base
import datetime

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

    def get_password(self, login):
        self.cursor.execute("select password from users where login = %s", (login))
        return self.cursor.fetchall()

    def get_banlist(self, login):
        self.cursor.execute("select id_ban from bans_to_users where id_user = (select id from users where login = %s)", (login))
        return self.cursor.fetchall()

    def get_bans(self):
        self.cursor.execute("select id_ban, ban_name from bans")
        return self.cursor.fetchall()

    def add_ban(self, id_ban, login):
        self.connection.begin()
        self.cursor.execute("INSERT INTO bans_to_users (id_user, id_ban) VALUES ((select id_user from users where login = %s), %s)", (login, id_ban))
        self.connection.commit()

    def drop_ban(self, id_ban, login):
        self.connection.begin()
        self.cursor.execute("DELETE FROM bans_to_users where id_user = (select id_user from users where login = %s) and id_ban = %s", (login, id_ban))
        self.connection.commit()
        
    def get_cc_payment(self, login):
        self.cursor.execute("select cc_payment from users where user_;ogin = %s", (login))
        return self.cursor.fetchall()

    def clear_cc_payment(self, login):
        self.connection.begin()
        self.cursor.execute("UPDATE users SET cc_payment = 0 WHERE login = %s;", (login))
        self.connection.commit()

    def start_user_session(self, login):
        self.connection.begin()
        self.cursor.execute("INSERT INTO sessions (id_user, start) VALUES ((select id_user from users where login = %s), %s)", (login, datetime.datetime.now()))
        self.connection.commit()
        self.cursor.execute("select LAST_INSERT_ID()")
        return  self.cursor.fetchall()

    def end_user_session(self, session):
        self.connection.begin()
        self.cursor.execute("UPDATE sessions SET end = %s WHERE id_session = %s;", (datetime.datetime.now(), session))
        self.connection.commit()    
        
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
