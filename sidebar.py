import kivy
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button

class Sidebar(StackLayout):
    def shop(self, instance):
        print("adding a button")
        self.add_widget(Button())
