import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

kivy.require('1.10.1')

Builder.load_file('loginscreen.kv')
Builder.load_file('registerscreen.kv')
Builder.load_file('mainscreen.kv')
Builder.load_file('searchresultsscreen.kv')

class MyScreenManager(ScreenManager):
    pass

class TuneDuneApp(App):
    def build(self):
        return MyScreenManager()

if __name__ == '__main__':
    TuneDuneApp().run()
