import kivy
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


