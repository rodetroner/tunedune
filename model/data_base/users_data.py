import dbase
import datetime
import sys

sys.path.append('../exceptions_d')

from dbase import Data_Base
from pymysql.err import MySQLError
from exceptions import Ex_Handler

class Users_data():
    """Class for handeling operations on data regarding users.
    """
    def __init__(self):
        self.db = dbase.Data_Base()
        self.db.connect_to_data_base()
        self.connection = self.db.get_connection()
        self.cursor = self.db.db_cursor

    def get_users(self, username = '', email = ''):
        """Returns datas needed for creation of objects representing userss as a list
        """
        if username == '' and email == '':
            try:
                self.cursor.execute("select login, email, balance from users")
            except (MySQLError):
                Ex_Handler.call('Data base error')
            return
        else:
            try:
                if username == '': 
                    self.cursor.execute("select login, email, balance from users where email = %s", (email))
                if email == '': 
                    self.cursor.execute("select login, email, balance from users where login = %s", (username))
            except (MySQLError):
                Ex_Handler.call('Data base error')
            else:
                return self.cursor.fetchall()

    def get_password(self, login):
        """Returnss hashed password as a list for given login. 
        """
        try:
            self.cursor.execute("select password from users where login = %s", (login))
        except (MySQLError):
            Ex_Handler.call('Data base error')
        else:
            return self.cursor.fetchall()

    def get_banlist(self, login):
        """Returnss list of bans/permisions for user as a list for given login. 
        """
        self.cursor.execute("select id_ban from bans_to_users where id_user = (select id_user from users where login = %s)",
                            (login)
                            )
        return self.cursor.fetchall()

    def get_bans(self):
        """Returns a list of lists of ids and names of all bans/permissions.
        """
        try:
            self.cursor.execute("select id_ban, ban_name from bans")
        except (MySQLError):
            Ex_Handler.call('Data base error')
        else:
            return self.cursor.fetchall()

    def add_ban(self, id_ban, login):
        """Adds a ban to user.
        """
        try:
            self.connection.begin()
            self.cursor.execute("INSERT INTO bans_to_users (id_user, id_ban)\
                                VALUES ((select id_user from users where login = %s), %s)",
                                (login, id_ban)
                                )
        except (MySQLError):
            Ex_Handler.call('Data base error')
        else:
            self.connection.commit()

    def drop_ban(self, id_ban, login):
        """Removes position from ban list for user.
        """
        try:
            self.connection.begin()
            self.cursor.execute("DELETE FROM bans_to_users where id_user = (select id_user from users where login = %s) \
                                and id_ban = %s", (login, id_ban))
        except (MySQLError):
            Ex_Handler.call('Data base error')
        else:
            self.connection.commit()
        
    def get_cc_payment(self, login):
        """If user has certain permissions they can have certain amount of money to pay to them.
        This method returns that amount.
        """
        try:
            self.cursor.execute("select cc_payment from users where user_;ogin = %s", (login))
        except (MySQLError):
            Ex_Handler.call('Data base error')
        else:
            return self.cursor.fetchall()

    def clear_cc_payment(self, login):
        """Sets payment_cc to 0.
        """
        try:
            self.connection.begin()
            self.cursor.execute("UPDATE users SET cc_payment = 0 WHERE login = %s;", (login))
        except (MySQLError):
            Ex_Handler.call('Data base error')
        else:
            self.connection.commit()

    def start_user_session(self, login):
        """Inserts to DB info about session start and returns its id.
        """
        try:
            self.connection.begin()
            self.cursor.execute("INSERT INTO sessions (id_user, start)\
                                VALUES ((select id_user from users where login = %s), %s)",
                                    (
                                     login,
                                     datetime.datetime.now()
                                    )
                                )
        except (MySQLError):
            Ex_Handler.call('Data base error')
        else:
            self.connection.commit()
        try:
            self.cursor.execute("select LAST_INSERT_ID()")
        except (MySQLError):
            Ex_Handler.call('Data base error')
        else:
            return  self.cursor.fetchall()

    def end_user_session(self, session):
        """Updates row of current session with end time.
        """
        try:
            self.connection.begin()
            self.cursor.execute("UPDATE sessions SET end = %s WHERE id_session = %s;",
                                    (
                                     datetime.datetime.now(),
                                     session
                                    )
                                )
        except (MySQLError):
            Ex_Handler.call('Data base error')
        else:
            self.connection.commit()    
        
    def add_user(self, username = '', email = '', password = ''):
        """Inserts to data base record widh data regarding new user.
        """    
        if username == '' or email == '' or email == '':
            return 0
        else:
            try:
                self.connection.begin()
                self.cursor.execute("INSERT INTO users (login, password, email) VALUES (%s, %s, %s)",
                                    (username, password, email)
                                    )
            except (MySQLError):
                Ex_Handler.call('Data base error')
            else:
                self.connection.commit()
                return 1

    def alter_user(self, login, username = '', email = '', password = '', balance_change = 0):
        """Changes data in database, regarding user with given id.
        """
        if username == '' and email == '' and email == '' and balance_change == 0:
            return 0
        else:
            try:
                self.connection.begin()
                if username != '':
                    self.cursor.execute("UPDATE users SET login = %s WHERE login = %s;", (username, login))
                if password != '':
                    self.cursor.execute("UPDATE users SET password = %s WHERE login = %s;", (password, login))
                if email != '':
                    self.cursor.execute("UPDATE users SET email = %s WHERE login = %s;", (email, login))
                if balance_change != 0:
                    self.cursor.execute("UPDATE users SET balance = balance + %s WHERE login = %s;",
                                        (balance_change, login)
                                        )
            except (MySQLError):
                Ex_Handler.call('Data base error')
            else:
                self.connection.commit()
            return 1

    def delete_user(self, username):
        """Removes data from data base of user with provided login.
        """
        if username == '':
            return 0
        else:
            try:
                self.connection.begin()
                self.cursor.execute("DELETE FROM users WHERE login = %s", (username))
            except (MySQLError):
                Ex_Handler.call('Data base error')
            else:
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
