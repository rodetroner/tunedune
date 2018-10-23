import vlc
import time
import kivy
kivy.require('1.10.1')
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import *
from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior

class My_Button(ButtonBehavior, Image):
    def __init__(self, path, function = None, **kwargs):
        super(My_Button, self).__init__(**kwargs)
        self.source = path
        self.function = function

    def on_press(self):
        self.function()

class Player:
    def __init__(self, path):
        self.__instance = vlc.Instance()
        self.__media = False
        self.__player = False
        self.__path = path
    
    def play_track(self):
        self.__player = self.__instance.media_player_new()      #creating instance of MP
        self.__media = self.__instance.media_new(self.__path)   #create instance of media
        self.__player.set_media(self.__media)                   #load file into player
        self.__player.play()                                    #play file
        

class Player_Window(Widget):
    def __init__(self, path, **kwargs):
        super(Player_Window, self).__init__(**kwargs)
        self._disabled_count = 0
        __player = Player(path)                                 #create instance of Player
        self.button_play = My_Button('playbutton.png', __player.play_track)
        self.add_widget(self.button_play)

class Player_App(App):
    def __init__(self, path, **kwargs):
        self._path = path
        super(Player_App, self).__init__(**kwargs)
        
    def build(self):
        return Player_Window(self._path)
        

Player_App('test.mp3').run()                                             #uncomment to test
