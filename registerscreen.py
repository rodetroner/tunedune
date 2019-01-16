import kivy
import sys
sys.path.append('./model')
sys.path.append('./model/data_base')
sys.path.append('./model/exceptions_d')
import user_d.user
from kivy.uix.screenmanager import Screen

kivy.require('1.10.1')

class RegisterScreen(Screen):
    def register(self, instance, *args):
        if self.password_input == self.confirm_password_input:
            if user_d.user.User.regiester(
                    self.username_input.text,
                    self.password_input.text,
                    self.email_input.text):
                print('registration successful')
            else:
                print('registration unsuccessful')
