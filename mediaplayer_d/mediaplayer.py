import kivy

kivy.require('1.10.1')

import sys

sys.path.append('../model/exceptions_d')
sys.path.append('../track_screen')

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from player_view import *
from player_model import *
from vlc import VLCException
from kivy.uix.widget import WidgetException
from kivy.uix.screenmanager import Screen
from exceptions import *
from kivy.uix.boxlayout import BoxLayout

class Player_Window(FloatLayout):
    """Class that defines, binds and contais all of mediaplayers features. Only two instances may exist in app.
    """
    def __init__(self, path, cover_path, **kwargs):
        """If valid paths were provided constructor will call for method that will create window for app.
        """
        self._disabled_count = 0
        self._attempts = 0
        if not (path == "" and cover_path == ""):
            self.reset_player(path, cover_path)

    def reset_player(self, path, cover_path):
        """Based on paths provided creates and adds elements to window of a player.

        Instance of Player is created here as well as all GUI elements. It also binds methods to GUI elements.
        Starts dispatcher for progress slider movement. At the begining clears previously created window.
        """
        try:
            print(path)
            super(Player_Window, self).__init__()
            self.clear_widgets()
            self.player_w = Player(path)
            self.player_w.play_track()
            self.player_w.player.audio_set_volume(25)
            self.cover = Display_area(cover_path)
            self.button_play = My_toggle_btn('../mediaplayer_d/playbutton.png',
                                             self.player_w.player.play,
                                             path2 = '../mediaplayer_d/stopbutton.png',
                                             function2 = self.player_w.player.pause,
                                             get_length = self.player_w.player.get_length,
                                             get_time = self.player_w.player.get_time
                                             ) 
            self.forward = My_Button('../mediaplayer_d/forwardbutton.png',
                                     self.player_w.forward_5_sec
                                     )
            self.backwards = My_Button('../mediaplayer_d/backwardsbutton.png',
                                       self.player_w.backwards_5_sec
                                       )
            self.volume_slider = Volume_Slider(self.player_w.player.audio_set_volume)
            self.button_repeat = My_Button('../mediaplayer_d/repeatbutton.png',
                                           lambda: self.player_w.repeat(self.button_play))
            self.media_slider = Media_Slider(self.player_w.player.set_position,
                                             self.player_w.player.is_playing,
                                             self.player_w.player.get_time,
                                             self.player_w.player.get_length)
            self.volume_icon = My_Button('../mediaplayer_d/volume.png', lambda: None)
            self.cover.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
            self.button_repeat.pos_hint = {'center_x': 0.1, 'center_y': 0.1}
            self.backwards.pos_hint = {'center_x': 0.2, 'center_y': 0.1}
            self.button_play.pos_hint = {'center_x': 0.3, 'center_y': 0.1}
            self.forward.pos_hint = {'center_x': 0.4, 'center_y': 0.1}
            self.volume_icon.pos_hint = {'center_x': 0.55, 'center_y': 0.1}
            self.volume_slider.pos_hint = {'center_x': 0.7, 'center_y': 0.1}
            self.volume_slider.size_hint = (0.2, 0.05)
            self.media_slider.size_hint = (1, 0.05)
            self.button_play.size_hint = (0.1, 0.1)
            self.volume_icon.size_hint = (0.1, 0.1)
            self.backwards.size_hint = (0.1, 0.1)
            self.forward.size_hint = (0.1, 0.1)
            self.button_repeat.size_hint = (0.1, 0.1)
            self.media_slider.pos_hint = {'center_x': 0.5, 'center_y': 0.2}
            self.media_slider.sensitivity = 'handle'
            self.volume_slider.sensitivity = 'handle'
            self.add_widget(self.cover)
            self.add_widget(self.media_slider)
            self.add_widget(self.volume_slider)
            self.add_widget(self.button_repeat)
            self.add_widget(self.backwards)
            self.add_widget(self.button_play)
            self.add_widget(self.forward)
            self.add_widget(self.volume_icon)
            self.media_slider.start_clock()
        except (VLCException, widget):
            if(self._attempts < 3):
                self._attempts = self._attempts + 1
                self.reset_player(path, cover_path)
            else:
                Ex_Handler.call('Something went wrong while building player, try again')
        else:
            self._attempts = 0
  
class Player_App(Screen):
    """Class that will run application of mediaplayer.
    """
    player_pool = list((Player_Window("", ""), Player_Window("", "")))
    
    def __init__(self, ms,**kwargs):
        #resources.resource_add_path("path to folder where stored")
        #uncomment and fill after fetching files from server is done!!!!!!
        super(Player_App, self).__init__(name = 'Player')
        '''try:
            if path == '':
                raise PA_Exception()
        except (PA_Exception):
            Ex_Handler.call("Invalid path, start taking pension for it!")
            return
        self._path = path
        self._cover_path = cover_path'''
        self.p = Player_App.get_player('','')
        LB = BoxLayout(orientation = 'vertical')
        LB2 = BoxLayout(orientation = 'horizontal')
        LB2.add_widget(My_Button1(lambda i: ms("Tracks"), 1, text = '<'))
        LB2.add_widget(My_Button1(lambda i: ms('Playlist'), 1, text = '>'))
        LB2.size_hint = (1, 0.2)
        LB2.height = 20
        LB.add_widget(LB2)
        LB.add_widget(self.p)
        self.add_widget(LB)
        
    '''def build(self):
        """Method for building up materials that its supposed to run.
        """
        self._player_window = Player_App.get_player(self._path, self._cover_path)
        return self._player_window'''
    
    '''def on_stop(self):
        """Actions on window's closing.
        """
        self._player_window.player_w.player.stop()
        Player_App.free_player(Player_App, self._player_window)'''

    @classmethod
    def get_player(cls, path, cover):
        """Method to get object of Window_Player from pool.
        """
        try:
            if Player_App.player_pool == []:
                raise OP_Exception('You already have maximum windows with player open')
            else:
                Player_App.player_pool[0].reset_player(path, cover)
                return Player_App.player_pool.pop(0)
        except OP_Exception as e:
            Ex_handler.call(e)

    def free_player(cls, p):
        """Returns Player_Window to pool.
        """
        Player_App.player_pool.append(p)

#if __name__ == '__main__':
#    Player_App('test.mp3', '').run()           #uncomment to test
