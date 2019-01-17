import kivy
import datetime
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

sys.path.append('../mediaplayer_d')
sys.path.append('../playlist_screen')
sys.path.append('../model/track_d')
sys.path.append('../model/album_d')
sys.path.append('../model/data_base')
sys.path.append('../model/actions_d')
sys.path.append('../model/exceptions_d')
sys.path.append('../model/transactions_d')
sys.path.append('../model')
sys.path.append('../model/user_d')
sys.path.append('../tunedune')
kivy.require('1.10.1')
Builder.load_file('a_screen.kv')

import mediaplayer
import pl_screen
import ac_screen
import t_screen
from album import *
from track import *
from actions import *
import actions

class MyLabelWithBackground(Label):
    pass

class MyLabelWithBackground1(Label):
    pass

class My_Button1(Button, ButtonBehavior):
    def __init__(self, function, arg, flag, **kwargs):
        super(My_Button1, self).__init__(**kwargs)
        self.arg = arg
        self.function = function
        self.flag = flag

    def on_press(self):
        self.function(self.arg)
        if self.flag == 1:
            #ms.transition = 'right'
            ms.current = "Playlist"

class A_Screen(Screen):
    def __init__(self, set_ms_curr, album_reset = None):
        super(A_Screen, self).__init__(name = 'Albums')
        #print('asdfg')
        i = 0
        LB = BoxLayout(orientation = 'vertical')
        LB2 = BoxLayout(orientation = 'horizontal')
        LB2.add_widget(My_Button1(lambda i: set_ms_curr(''), 1, 0, text = '<'))
        LB2.add_widget(My_Button1(lambda i: set_ms_curr("Playlist"), 1, 0, text = '>'))
        LB.add_widget(LB2)
        LB.add_widget(Label(text = 'Albums searched'))
        #print(curr_searched_album_list)
        while i < len(curr_searched_album_list):
            #print('a')
            temp = BoxLayout(orientation = 'horizontal')
            temp.size_hint = (1, 1)
            temp.height = 20
            l = curr_searched_album_list[i].get_album_name()
            if i % 2 == 0:
                lab = MyLabelWithBackground(text = l)
            else:
                lab = MyLabelWithBackground1(text = l)
            temp.add_widget(lab)
            btn1 = My_Button1(lambda i: curr_searched_album_list[i].buy(User('test'), datetime.datetime.now()), i, 0, text = 'Buy')
            temp.add_widget(btn1)
            btn2 = My_Button1(lambda i: set_ms_curr("Playlist", curr_searched_album_list[i], fun = album_reset), i, 1, text = 'Play')
            temp.add_widget(btn2)
            i += 1
            LB.add_widget(temp)
        sv = ScrollView(size_hint=(1, None), size=(Window.width, Window.height))
        sv.add_widget(LB)
        self.add_widget(sv)

class MyScreenManager(ScreenManager):
    def __init__(self):
        super(MyScreenManager, self).__init__()

    def add(self):
        self.add_widget(t)
        self.add_widget(pl)
        self.add_widget(a)
        self.add_widget(ac)
        self.add_widget(a2)
        self.add_widget(t2)

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
a = mediaplayer.Player_App(ms.set_ms_curr, 'Player')
a2 = mediaplayer.Player_App(ms.set_ms_curr, 'Player_ads')
pl = pl_screen.Pl_Screen(ms.set_ms_curr, a)
t = A_Screen(ms.set_ms_curr, album_reset = pl.reset)
t2 = t_screen.T_Screen(ms.set_ms_curr, a)
ac = ac_screen.Ac_Screen(ms.set_ms_curr, a2)
ms.add()
TuneDuneApp().run()
