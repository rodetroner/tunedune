import kivy
import sys
sys.path.append('./model')
sys.path.append('./model/data_base')
sys.path.append('./model/exceptions_d')
import user_d.user
from kivy.uix.screenmanager import Screen

kivy.require('1.10.1')

class MainScreen(Screen):
    def logOut(self, instance, *args):
        print(self.login_screen.current_session)
        
