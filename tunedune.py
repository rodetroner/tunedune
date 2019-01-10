import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from loginscreen import LoginScreen
from mainscreen import MainScreen

kivy.require('1.10.1')

Builder.load_file('sidebar.kv')
Builder.load_file('loginscreen.kv')
Builder.load_file('mainscreen.kv')

class TuneDuneApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login_scr'))
        sm.add_widget(MainScreen(name='main_scr'))
        return sm

if __name__ == '__main__':
    TuneDuneApp().run()
