import sys
sys.path.append('../data_base')
from argon2 import PasswordHasher
from users_data import Users_data as user

class User:
    def __init__(self, login):
        a = Users_data().get_users(username = login)
        self.login = a[0][0]
        self.email = a[0][1]
        self.balance = a[0][2]
        self.banlist = Users_data().get_banlist(self.login)

    def alter_user(self, login = '', email = '', passwordd = '', balance = 0):
        if balance > self.balance:
            return 0
        Users_data().alter_user(self.login, login = login, email = emai, passwordd = passwordd, balance_change = balance)
        return 1
        
    @classmethod
    def login(cls, login, password):
        a = Users_data().get_users(username = login)
        hashed = Users_data().get_password(a[0])
        if PasswordHasher().verify(hashed[0], password):
            Users_data().start_user_session(login)
            return 1
        return 0
    
    @classmethod
    def regiester(cls, login, password, email):
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
        Users_data().end_user_session()
              
        
        
        


