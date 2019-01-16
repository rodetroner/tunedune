import kivy
import sys
sys.path.append('./model')
sys.path.append('./model/data_base')
sys.path.append('./model/exceeptions_d')
import user_d.user
from kivy.uix.screenmanager import Screen
kivy.require('1.10.1')

class LoginScreen(Screen):

    ''' Clear the login text field unless, the user typed their username '''
    def clearLogin(self, instance, *args):
        if self.login_input.text == 'Username':
            self.login_input.text = ''

    ''' Clear the password text field unless, the user typed their username
        and mask the input '''
    def clearPassword(self, instance, *args):
        if self.password_input.text == 'Password':
            self.password_input.text = ''
            self.password_input.password = True
    
    def logInAction(self, instance, *args):
        self.current_session = user_d.user.User.login(self.login_input.text,
                                                self.password_input.text)
        print('login_succesful')
