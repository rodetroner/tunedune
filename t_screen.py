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
import sys

sys.path.append('../mediaplayer_d')
sys.path.append('../model/track_d')
sys.path.append('../model/data_base')
sys.path.append('../model/exceptions_d')
sys.path.append('../model/transactions_d')
sys.path.append('../model')
sys.path.append('../model/user_d')
kivy.require('1.10.1')
Builder.load_file('a_screen.kv')

ms = None

import mediaplayer
from track import *

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
            ms.current = "Player"

class T_Screen(Screen):
    def __init__(self, set_ms_curr, a):
        super(T_Screen, self).__init__(name = 'Tracks')
        i = 0
        LB = BoxLayout(orientation = 'vertical')
        LB2 = BoxLayout(orientation = 'horizontal')
        LB2.add_widget(My_Button1(lambda i: set_ms_curr('MainScreen'), 1, 0, text = '<'))
        LB2.add_widget(My_Button1(lambda i: set_ms_curr("Player"), 1, 0, text = '>'))
        LB.add_widget(LB2)
        LB.add_widget(Label(text = 'Tracks searched'))
        
        while i < len(curr_searched_track_list):
            temp = BoxLayout(orientation = 'horizontal')
            temp.size_hint = (1, 1)
            temp.height = 20
            l = curr_searched_track_list[i].get_track_name() + " by: " + curr_searched_track_list[i].get_authors()[0][0]
            if i % 2 == 0:
                lab = MyLabelWithBackground(text = l)
            else:
                lab = MyLabelWithBackground1(text = l)
            temp.add_widget(lab)
            btn1 = My_Button1(lambda i: curr_searched_track_list[i].buy(User('test'), datetime.datetime.now()), i, 0, text = 'Buy: ' + str(curr_searched_track_list[i].get_track_price()))
            temp.add_widget(btn1)
            btn2 = My_Button1(lambda i:  curr_searched_track_list[i].play_track(a), i, 1, text = 'Play')
            temp.add_widget(btn2)
            i += 1
            LB.add_widget(temp)
        sv = ScrollView(size_hint=(1, None), size=(Window.width, Window.height))
        sv.add_widget(LB)
        self.add_widget(sv)
"""        
class MyScreenManager(ScreenManager):
    def __init__(self):
        super(MyScreenManager, self).__init__()

    def add(self):
        self.add_widget(t)
        self.add_widget(a)

    def set_ms_curr(self, s):
        if s != '': 
            ms.current = s
    
class TuneDuneApp(App):
    def build(self):
        return ms

search_track()
ms = MyScreenManager()
a = Player_App(ms.set_ms_curr)
t = T_Screen()
screens = [a, t]
ms.add()
TuneDuneApp().run()"""
