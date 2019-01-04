import kivy
kivy.require('1.10.1')

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.anchorlayout import AnchorLayout

Builder.load_file('sidebar.kv')
Builder.load_file('tracklist.kv')

class MainLayout(AnchorLayout):
    pass

class TuneDuneApp(App):
    def build(self):
        return MainLayout()

if __name__ == '__main__':
    TuneDuneApp().run()
