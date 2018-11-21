import kivy
kivy.require('1.10.1')

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class MyWindow(BoxLayout):
    pass

class TuneDuneApp(App):
    def build(self):
        return MyWindow()

if __name__ == '__main__':
    TuneDuneApp().run()
