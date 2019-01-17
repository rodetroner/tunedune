import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.uix.label import Label
import sys

sys.path.append('./mediaplayer_d')
sys.path.append('./playlist_screen')
sys.path.append('./model/track_d')
sys.path.append('./model/album_d')
sys.path.append('./model/data_base')
sys.path.append('./model/actions_d')
sys.path.append('./model/exceptions_d')
sys.path.append('./model/transactions_d')
sys.path.append('./model')
sys.path.append('./model/user_d')

kivy.require('1.10.1')

Builder.load_file('loginscreen.kv')
Builder.load_file('registerscreen.kv')
Builder.load_file('mainscreen.kv')
Builder.load_file('searchresultsscreen.kv')
Builder.load_file('a_screen.kv')

import mediaplayer
import pl_screen
import ac_screen
import t_screen
import a_screen
import u_screen
import loginscreen
import mainscreen
import registerscreen
from album import *
from track import *
from actions import *
import actions

class MyScreenManager(ScreenManager):
    def __init__(self):
        super(MyScreenManager, self).__init__()

    def add(self):
        self.add_widget(loginscreen.LoginScreen(name = 'LoginScreen'))
        self.add_widget(mainscreen.MainScreen(name = 'MainScreen'))
        self.add_widget(t)
        self.add_widget(pl)
        self.add_widget(a)
        self.add_widget(ac)
        self.add_widget(a2)
        self.add_widget(t2)
        self.add_widget(registerscreen.RegisterScreen(name = 'RegisterScreen'))

    def set_ms_curr(self, s, album = None, fun = None):
        if s != '': 
            ms.current = s
        if album:
            if fun:
                fun(album)

class TuneDuneApp(App):
    def build(self):
        return ms

search_album()
search_track()
search_ads()
ms = MyScreenManager()
pl_screen.ms = ms
t_screen.ms = ms
a_screen.ms = ms
ac_screen.ms = ms
u = u_screen.U_Screen(ms.set_ms_curr)
a = mediaplayer.Player_App(ms.set_ms_curr, 'Player')
a2 = mediaplayer.Player_App(ms.set_ms_curr, 'Player_ads')
pl = pl_screen.Pl_Screen(ms.set_ms_curr, a)
t = a_screen.A_Screen(ms.set_ms_curr, album_reset = pl.reset)
t2 = t_screen.T_Screen(ms.set_ms_curr, a)
ac = ac_screen.Ac_Screen(ms.set_ms_curr, a2)

ms.add()
#ms.current = 'LoginScreen'
TuneDuneApp().run()
