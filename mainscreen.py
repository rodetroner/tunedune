import kivy
import sys
sys.path.append('./model')
import user_d.user
from kivy.uix.screenmanager import Screen

kivy.require('1.10.1')

class MainScreen(Screen):
    def logOut(self, instance, *args):
        print(self.login_screen.current_session)
        
