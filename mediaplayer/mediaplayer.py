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
from kivy.uix.boxlayout import BoxLayout

class My_Button(ButtonBehavior, Image):
    def __init__(self, path1, function1 = None, path2 = None, function2 = None, toogle = False, **kwargs):
        super(My_Button, self).__init__(**kwargs)
        self.source = path1
        self.path1 = path1
        self.path2 = path2
        self.function = function1
        self.function1 = function1
        self.function2 = function2
        self.version = 0
        self.toogleable = toogle

    def on_press(self):
        self.function()
        if self.toogleable:
            self.toogle()

    def toogle(self):
        if self.version == 0:
            self.version = 1
            self.source = self.path2
            self.function = self.function2
        else:
            self.version = 0
            self.source = self.path1
            self.function = self.function1
            
class Player:
    def __init__(self, path):
        self.__instance = vlc.Instance()
        self.__media = None
        self.player = None
        self.__path = path
    
    def play_track(self):
        self.player = self.__instance.media_player_new()      #creating instance of MP
        self.__media = self.__instance.media_new(self.__path)   #create instance of media
        self.player.set_media(self.__media)                   #load file into player
        #self.__player.play()                                    #play file

    def forward_5_sec(self):
        length = self.player.get_length()
        if self.player.get_time() + 5000 > length:
            self.player.set_position(1)
            return 0
        x = 5000 / length
        self.player.set_position(self.player.get_position() + x)

    def backwards_5_sec(self):
        if self.player.get_time() < 5000:
            self.player.set_position(0)
            return 0
        length = self.player.get_length()
        x = 5000 / length
        self.player.set_position(self.player.get_position() - x)
        
class Player_Window(BoxLayout):
    def __init__(self, path, **kwargs):
        super(Player_Window, self).__init__(orientation = 'horizontal')
        self._disabled_count = 0
        self.player_w = Player(path)                                 #create instance of Player
        self.player_w.play_track()
        self.button_play = My_Button('playbutton.png', self.player_w.player.play, 'stopbutton.png', self.player_w.player.pause, toogle = True)
        self.add_widget(self.button_play)
        self.forward = My_Button('forwardbutton.png', self.player_w.forward_5_sec)
        self.add_widget(self.forward)
        self.backwards = My_Button('backwardsbutton.png', self.player_w.backwards_5_sec)
        self.add_widget(self.backwards)
        
class Player_App(App):
    def __init__(self, path, **kwargs):
        self._path = path
        super(Player_App, self).__init__(**kwargs)
        
    def build(self):
        self._player_window = Player_Window(self._path)
        return self._player_window
    
    def on_stop(self):
        self._player_window.player_w.player.stop()

        

Player_App('test.mp3').run()                                             #uncomment to test
