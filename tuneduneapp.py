import kivy
kivy.require('1.10.1')

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.stacklayout import StackLayout

class MyWindow(StackLayout):
    pass

class TuneDuneApp(App):
    def build(self):
        return MyWindow()

if __name__ == '__main__':
    TuneDuneApp().run()
