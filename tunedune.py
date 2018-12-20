import kivy
kivy.require('1.10.1')

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.stacklayout import StackLayout
from kivy.uix.anchorlayout import AnchorLayout

class MainLayout(AnchorLayout):
    pass

class TuneDuneApp(App):
    def build(self):
        return MainLayout()

if __name__ == '__main__':
    TuneDuneApp().run()
