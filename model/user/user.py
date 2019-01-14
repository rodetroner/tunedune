import sys

sys.path.append('../data_base')
sys.path.append('../exceptions')

from argon2 import PasswordHasher
from users_data import Users_data
from exceptions import Ex_Handler

class User:
    """Class aacts as fasade for module responsible for interacting with data base. 
    """
    def __init__(self, login):
        a = Users_data().get_users(username = login)
        try:
            if len(a) != 3:
                raise Ex_Data()
        except (Ex_Data):
            Ex_Handler.call('Data integrity error.')
            return
        self.login = a[0][0]
        self.email = a[0][1]
        self.balance = a[0][2]
        self.banlist = Users_data().get_banlist(self.login)

    def alter_user(self, login = '', email = '', password = '', balance = 0):
        if balance > self.balance:
            return 0
        Users_data().alter_user(self.login,
                                login = login,
                                email = emai,
                                password = password,
                                balance_change = balance)
        return 1

    def check_if_in_ban_list(self, x):
        """Method for checking if user has permission provided in arguments.
        """
        if x in banlist:
            return 1
        else:
            return 0

    @classmethod
    def alter_bans(self, id_ban, login, add = True):
        """Class method for changing permisions of user with given login.
        """
        if self.check_if_in_ban_list(x):
            return 0
        if add:
            Users_data().add_ban(id_ban, login)
        else:
            Users_data().drop_ban(id_ban, login)
        return 1
        
        
    @classmethod
    def login(cls, login, password):
        """Class method for handeling login to app.

        Compares password with the one from data base. Starts session.
        """
        a = Users_data().get_users(username = login)
        hashed = Users_data().get_password(a[0][0])
        print(hashed[0][0])
        if PasswordHasher().verify(hashed[0][0], password):
            return Users_data().start_user_session(login)
        return 0
    
    @classmethod
    def regiester(cls, login, password, email):
        """Puts given data into data base, hashes password.
        """
        tmp = Users_data()
        a = tmp.get_users(username = login)
        if a:
            return 0
        else:
            if password != '':
                password = PasswordHasher().hash(password)
                tmp.add_user(login, email, password)
                return 1
            else:
                return 0

    @classmethod
    def logout(session):
        """End session for user.
        """
        Users_data().end_user_session(session)

    @classmethod
    def get_users(username = '', email = ''):
        """Method returns a list of users with data like in arguments.
        """
        return Users_data().get_users(username, email)

