import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

kivy.require('1.10.1')

Builder.load_file('sidebar.kv')

class MainLayout(BoxLayout):
    pass

class TuneDuneApp(App):
    def build(self):
        return MainLayout()

if __name__ == '__main__':
    TuneDuneApp().run()
