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
from kivy.uix.textinput import TextInput
import sys

sys.path.append('../model/user_d')
sys.path.append('../model/data_base')
sys.path.append('../model/exceptions_d')
sys.path.append('../model/transactions_d')
sys.path.append('../model')
sys.path.append('../model/user_d')
sys.path.append('../model/transactions_d')
kivy.require('1.10.1')
Builder.load_file('a_screen.kv')

ms = None

from user import *
from payment_cc import *

current_user = User('test')

def dummy():
    pass

def foo(reset, inp):
    reset(inp[0], User(inp[1].text))

class MyLabelWithBackground(Label):
    pass

class MyLabelWithBackground1(Label):
    pass

class My_Button1(Button, ButtonBehavior):
    def __init__(self, function, fun2, arg, arg2 = current_user, **kwargs):
        super(My_Button1, self).__init__(**kwargs)
        self.function = function
        self.fun2 = fun2
        self.arg = arg
        self.arg2 = arg2
        
    def on_press(self):
        self.function()
        self.fun2(self.arg, self.arg2)

class U_Screen(Screen):
    def __init__(self, set_ms_curr):
        super(U_Screen, self).__init__(name = 'Tracks')
        self.reset(set_ms_curr)

    def reset(self, set_ms_curr, curr_user = current_user):
        self.clear_widgets()
        LB = BoxLayout(orientation = 'vertical')
        LB2 = BoxLayout(orientation = 'horizontal')
        LB2.add_widget(My_Button1(lambda i: set_ms_curr("Albums"), self.reset, set_ms_curr, text = '>'))
        LB.add_widget(LB2)
        LB.add_widget(Label(text = 'My account'))
        l = "Username: " + curr_user.username
        self.lab = MyLabelWithBackground(text = l)
        ti1 = TextInput(text = curr_user.username, multiline = False)
        btn2 = My_Button1(lambda: curr_user.alter_user(login = self.ti1.text.strip()), self.reset, set_ms_curr, text = 'Change username')
        LB2 = BoxLayout(orientation = 'horizontal')
        LB2.add_widget(self.lab)
        LB2.add_widget(ti1)
        LB2.add_widget(btn2)
        LB.add_widget(LB2)
        l = "E-mail: " + curr_user.email
        ti2 = TextInput(text = curr_user.email, multiline = False)
        self.lab1 = MyLabelWithBackground1(text = l)
        btn1 = My_Button1(lambda: curr_user.alter_user(email = self.ti2.text.strip()), self.reset, set_ms_curr, text = 'Change email')
        LB2 = BoxLayout(orientation = 'horizontal')
        LB2.add_widget(self.lab1)
        LB2.add_widget(ti2)
        LB2.add_widget(btn1)
        LB.add_widget(LB2)
        l = "Password: "
        ti3 = TextInput(text = '', multiline = False)
        self.lab1 = MyLabelWithBackground(text = l)
        btn3 = My_Button1(lambda: curr_user.alter_user(password = self.ti3.text.strip()), self.reset, set_ms_curr, text = 'Change password')
        LB2 = BoxLayout(orientation = 'horizontal')
        LB2.add_widget(self.lab1)
        LB2.add_widget(ti3)
        LB2.add_widget(btn3)
        LB.add_widget(LB2)
        l = "Balance: " + str(curr_user.balance)
        self.lab3 = MyLabelWithBackground1(text = l)
        btn8 = My_Button1(lambda: dummy(), self.reset, set_ms_curr, text = 'Top up')
        LB.add_widget(self.lab3)
        LB.add_widget(btn8)
        if ('cc',) in curr_user.banlist:
            l = "Balance: " + str(curr_user.balance)
            self.lab4 = MyLabelWithBackground1(text = l)
            btn4 = My_Button1(lambda: Payment_CC.pay_cc(curr_user.login, 1, None), self.reset, set_ms_curr, text = 'Get paid')
            LB.add_widget(self.lab4)
            LB.add_widget(btn4)
        if ('admin',) in current_user.banlist:
            l = "Find user: "
            ti5 = TextInput(text = '', multiline = False)
            self.lab5 = MyLabelWithBackground1(text = l)
            btn5 = My_Button1(lambda: dummy(), foo, self.reset, arg2 = [set_ms_curr, ti5] , text = 'Search')
            LB.add_widget(self.lab5)
            LB.add_widget(ti5)
            LB.add_widget(btn5)
            self.lab5a = MyLabelWithBackground1(text = 'Permissions/bans: ' + str(curr_user.banlist))
            LB.add_widget(self.lab5a)
            ti6 = TextInput(text = '', multiline = False)
            btn5 = My_Button1(lambda: dummy(), self.reset, set_ms_curr, arg2 = curr_user, text = 'Add/drop perm')            
        sv = ScrollView(size_hint=(1, None), size=(Window.width, Window.height))
        sv.add_widget(LB)
        self.add_widget(sv)
        print(curr_user.banlist)
'''       
class MyScreenManager(ScreenManager):
    def __init__(self):
        super(MyScreenManager, self).__init__()

    def add(self):
        self.add_widget(t)

    def set_ms_curr(self, s):
        if s != '': 
            ms.current = s
    
class TuneDuneApp(App):
    def build(self):
        return ms

ms = MyScreenManager()
t = U_Screen(ms.set_ms_curr)
ms.add()
TuneDuneApp().run()
'''
