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
sys.path.append('../model/actions_d')
sys.path.append('../model/data_base')
sys.path.append('../model/exceptions_d')
sys.path.append('../model/transactions_d')
sys.path.append('../model')
sys.path.append('../model/user_d')

kivy.require('1.10.1')
#Builder.load_file('../tunedune/actions_screen/ac_screen.kv')

import mediaplayer
import actions

#print(list_of_schearched_ads)

class MyLabelWithBackground(Label):
    pass

class MyLabelWithBackground1(Label):
    pass

ms = None

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
            ms.current = "Player_ads"

class Ac_Screen(Screen):
    def __init__(self, set_ms_curr, player_screen):
        super(Ac_Screen, self).__init__(name = 'Ads')
        i = 0
        LB = BoxLayout(orientation = 'vertical')
        LB2 = BoxLayout(orientation = 'horizontal')
        LB2.add_widget(My_Button1(lambda i: set_ms_curr(''), 1, 0, text = '<'))
        LB2.add_widget(My_Button1(lambda i: set_ms_curr("Player_ads"), 1, 0, text = '>'))
        LB.add_widget(LB2)
        LB.add_widget(Label(text = 'Ads searched'))
        
        while i < len(actions.list_of_schearched_ads):
            temp = BoxLayout(orientation = 'horizontal')
            temp.size_hint = (1, 1)
            temp.height = 20
            l = actions.list_of_schearched_ads[i].name + " by: " + actions.list_of_schearched_ads[i].provider
            if i % 2 == 0:
                lab = MyLabelWithBackground(text = l)
            else:
                lab = MyLabelWithBackground1(text = l)
            temp.add_widget(lab)
            btn1 = My_Button1(lambda i: actions.list_of_schearched_ads[i].run_ad(player_screen), i, 1)
            temp.add_widget(btn1)
            i += 1
            LB.add_widget(temp)
        sv = ScrollView(size_hint=(1, None), size=(Window.width, Window.height))
        sv.add_widget(LB)
        self.add_widget(sv)
'''
class MyScreenManager(ScreenManager):
    def __init__(self):
        super(MyScreenManager, self).__init__()

    def add(self):
        self.add_widget(t)
        self.add_widget(ad)

    def set_ms_curr(self, s):
        if s != '': 
            ms.current = s
    
class TuneDuneApp(App):
    def build(self):
        return ms

search_ads()
ms = MyScreenManager()
ad = Player_App(ms.set_ms_curr, 'Player_ads')
t = Ac_Screen(ms.set_ms_curr, ad)
ms.add()
TuneDuneApp().run()
'''
