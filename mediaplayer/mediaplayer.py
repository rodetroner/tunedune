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
from kivy.uix.slider import Slider
import copy

class My_Sliders(Slider):
    def __init__(self, method_set, initial_value):     #passing methods so no need for passing player
        super(My_Sliders, self).__init__(min = 0, max = 100, value = initial_value)
        self.method_set = method_set

class Volume_Slider(My_Sliders):
    def __init__(self, method_set):     #passing methods so no need for passing player
        super(Volume_Slider, self).__init__(method_set = method_set, initial_value = 25)

    def on_touch_up(self, touch):
        released = super(Volume_Slider, self).on_touch_up(touch) 
        if released:
            self.method_set(int(self.value))
                        
class Media_Slider(My_Sliders):
    def __init__(self, method_set):
        super(Media_Slider, self).__init__(method_set = method_set, initial_value = 0)
        self._is_touched = 0

    def on_touch_up(self, touch):
        self._is_touched = 1
        released = super(Media_Slider, self).on_touch_up(touch) 
        if released:
            self.method_set(int(self.value) / 100)
        self._is_touched = 0
        
    def change_state(self, method_get_time):
        if(self._is_touched == 0):
            self.value = method_get_time() * 100

def change_slider_state(method_change_state, method_get_time):
    while(method_get_time() != 100):
        method_change_state(method_get_time)

class My_Button(ButtonBehavior, Image):
    def __init__(self, path1, function1 = None, path2 = None, function2 = None, toogle = False, player = None, **kwargs):
        super(My_Button, self).__init__(**kwargs)
        self.source = path1
        self.path1 = path1
        self.path2 = path2
        self.function = function1
        self.function1 = function1
        self.function2 = function2
        self.version = 0
        self.toogleable = toogle
        self.player = copy.copy(player)

    def on_press(self):
        self.function()
        if self.toogleable:
            print(self.player.player.get_position())
            if self.player != None and self.player.player.get_position() < 1:   
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
        #self.__player.play()                                   #play file
        #print(self.player.audio_get_volume())

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

    def repeat(self, pb):
        self.player.pause()
        #if self.player.get_position() < 1:
        #    self.player.set_position(0)           
        #else:
        print('x')
        self.player.set_position(0)
        self.player.set_media(self.__media)
        self.player.set_position(0)
        self.player.play()
        pb.version = 1
        pb.source = pb.path2
        pb.function = pb.function2
        
        
class Player_Window(BoxLayout):
    def __init__(self, path, **kwargs):
        super(Player_Window, self).__init__(orientation = 'horizontal')
        self._disabled_count = 0
        self.player_w = Player(path)                                 #create instance of Player
        self.player_w.play_track()
        self.player_w.player.audio_set_volume(25)
        self.button_play = My_Button('playbutton.png', self.player_w.player.play, 'stopbutton.png', self.player_w.player.pause, toogle = True, player = self.player_w) 
        self.forward = My_Button('forwardbutton.png', self.player_w.forward_5_sec)
        self.backwards = My_Button('backwardsbutton.png', self.player_w.backwards_5_sec)
        self.volume_slider = Volume_Slider(self.player_w.player.audio_set_volume)
        self.button_repeat = My_Button('repeatbutton.png', lambda: self.player_w.repeat(self.button_play))
        self.media_slider = Media_Slider(self.player_w.player.set_position)
        self.add_widget(self.button_repeat)
        self.add_widget(self.backwards)
        self.add_widget(self.button_play)
        self.add_widget(self.forward)
        self.add_widget(self.volume_slider)
        self.add_widget(self.media_slider)
        
class Player_App(App):
    def __init__(self, path, **kwargs):
        self._path = path
        super(Player_App, self).__init__(**kwargs)
        
    def build(self):
        self._player_window = Player_Window(self._path)
        #change_slider_state(self._player_window.media_slider.change_state, self._player_window.player_w.player.get_position)
        return self._player_window
    
    def on_stop(self):
        self._player_window.player_w.player.stop()

        

Player_App('test.mp3').run()           #uncomment to test
