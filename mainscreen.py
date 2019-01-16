import kivy
import sys
sys.path.append('./model')
import user_d.user
from kivy.uix.screenmanager import Screen

kivy.require('1.10.1')

class MainScreen(Screen):
    def logOut(self, instance, *args):
        user_d.user.User.logout(self.login_screen.current_session)
        print(self.login_screen.current_session)
