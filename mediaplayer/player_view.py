import vlc
import time
import kivy
kivy.require('1.10.1')
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.image import AsyncImage
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.slider import Slider
from kivy.clock import Clock
import kivy.resources as resources

class Display_area(AsyncImage):
    def __init__(self, source):
        if resources.resource_find(source) == None:
            super(Display_area, self).__init__(source = 'default_bg_image.png')
        else:
            super(Display_area, self).__init__(source = source)

    def set_image(self, source):
        if resources.resource_find(source) == None:
            self.source = 'default_bg_image.png'
        else:
            self.source = source

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
    def __init__(self, method_set, track_is_playing, method_get_time, length):
        super(Media_Slider, self).__init__(method_set = method_set, initial_value = 0)
        self._is_touched = 0
        self.track_is_playing = track_is_playing
        self.track_length = length
        self.method_get_time = method_get_time

    def start_clock(self):
        Clock.schedule_interval(self.change_slider_state, 0.1)

    def on_touch_up(self, touch):
        self._is_touched = 1
        released = super(Media_Slider, self).on_touch_up(touch) 
        if released:
            self.method_set(int(self.value) / 100)
        self._is_touched = 0
        
    def change_state(self, method_get_time):
        if(self._is_touched == 0):
            self.value = method_get_time() * 100

    def change_slider_state(self, delta_time):
        if self.track_length() != -1:
            if self.track_is_playing() and self.method_get_time() < self.track_length():
                self.value = self.method_get_time() / self.track_length() * 100
        #print(self.method_get_time())


class My_Button(ButtonBehavior, Image):
    def __init__(self, path, function, **kwargs):
        super(My_Button, self).__init__(**kwargs)
        self.source = path
        self.function = function

    def on_press(self):
        self.function()

class My_toggle_btn(My_Button):
    def __init__(self, path1, function1, path2 = None, function2 = None, get_length= None, get_time = None, **kwargs):
        super(My_toggle_btn, self).__init__(path1, function1, **kwargs)
        self.source = path1
        self.path1 = path1
        self.path2 = path2
        self.function = function1
        self.function1 = function1
        self.function2 = function2
        self.version = 0
        self.player_get_time = get_time
        self.player_get_length = get_length
    
    def on_press(self):
        self.function()
        #print(self.player.player.get_length())
        if self.player_get_time() / (self.player_get_length() + 2**-10) < 1:   
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
    
