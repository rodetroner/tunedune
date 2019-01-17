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

class My_Button1(Button, ButtonBehavior):
    def __init__(self, function, arg, **kwargs):
        super(My_Button1, self).__init__(**kwargs)
        self.arg = arg
        self.function = function

    def on_press(self):
        self.function(self.arg)
            
class Display_area(AsyncImage):
    """A class for background/cover image of mediaplayer

    As it inharities properties from kivy's AsyncImage it only requires path to image file to display.
    """
    def __init__(self, source):
        if resources.resource_find(source) == None:
            super(Display_area, self).__init__(source = './mediaplayer_d/default_bg_image.png')
        else:
            super(Display_area, self).__init__(source = source)

    def set_image(self, source):
        """Allows to change image in widget.
        """
        if resources.resource_find(source) == None:
            self.source = './mediaplayer_d/default_bg_image.png'
        else:
            self.source = source

class My_Sliders(Slider):
    """Base class for sliders in mediaplayer.

    Instance is initiated as kivy Slider with addition of method to call and set value from interaction with.        
    """
    def __init__(self, method_set, initial_value):
        super(My_Sliders, self).__init__(min = 0, max = 100, value = initial_value)
        self.method_set = method_set

class Volume_Slider(My_Sliders):
    """Class meant for sliders handeling sound.

    Alhough it does not have any kind of build in interactions with MP's sound volume and bases that just on method passed, it is styled for it.
    """
    def __init__(self, method_set):
        super(Volume_Slider, self).__init__(method_set = method_set, initial_value = 25)

    def on_touch_up(self, touch):
        """Method overrides built in method of kivy slider and links slider to whatever passed method is related to.
        """
        released = super(Volume_Slider, self).on_touch_up(touch) 
        if released:
            self.method_set(int(self.value))
                        
class Media_Slider(My_Sliders):
    """Class meant for handeling slider as it moves with time.

    Methods in this class are meant mostly for handeling asynchronus task of sliders movement.
    """
    def __init__(self, method_set, track_is_playing, method_get_time, length):
        super(Media_Slider, self).__init__(method_set = method_set, initial_value = 0)
        self._is_touched = 0
        self.track_is_playing = track_is_playing
        self.track_length = length
        self.method_get_time = method_get_time

    def start_clock(self):
        """Starts the dispatcher for updating slider's position.
        """
        Clock.schedule_interval(self.change_slider_state, 0.1)

    def on_touch_up(self, touch):
        """Method overrides built in method of kivy slider and links slider to whatever passed method is related to.
        """
        self._is_touched = 1
        released = super(Media_Slider, self).on_touch_up(touch) 
        if released:
            self.method_set(int(self.value) / 100)
        self._is_touched = 0
        
    def change_state(self, method_get_time):
        """Changes current position according to time got from method passsed in arguments.
        """
        if(self._is_touched == 0):
            self.value = method_get_time() * 100

    def change_slider_state(self, delta_time):
        """Method called periodicly for updating slider.
        """
        if self.track_length() != -1:
            if self.track_is_playing() and self.method_get_time() < self.track_length():
                self.value = self.method_get_time() / self.track_length() * 100

class My_Button(ButtonBehavior, Image):
    """Class for button widgets in mediaplayer.
    """
    def __init__(self, path, function, **kwargs):
        super(My_Button, self).__init__(**kwargs)
        self.source = path
        self.function = function

    def on_press(self):
        self.function()

class My_toggle_btn(My_Button):
    """Class for buttons with 2 states.
    """
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
        if self.player_get_time() / (self.player_get_length() + 2**-10) < 1:   
            self.toogle()

    def toogle(self):
        """Method for changing state of button.
        """
        if self.version == 0:
            self.version = 1
            self.source = self.path2
            self.function = self.function2
        else:
            self.version = 0
            self.source = self.path1
            self.function = self.function1
