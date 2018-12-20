import kivy
kivy.require('1.10.1')
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from player_view import *
from player_model import *

class Player_Window(FloatLayout):
    def __init__(self, path, cover_path, **kwargs):
        super(Player_Window, self).__init__()
        self._disabled_count = 0
        self.reset_player(path, cover_path)

    def reset_player(self, path, cover_path):
        self.clear_widgets()
        self.player_w = Player(path)                                 #create instance of Player
        self.player_w.play_track()
        self.player_w.player.audio_set_volume(25)
        self.cover = Display_area(cover_path)
        self.button_play = My_toggle_btn('playbutton.png', self.player_w.player.play, path2 = 'stopbutton.png', function2 = self.player_w.player.pause, get_length = self.player_w.player.get_length, get_time = self.player_w.player.get_time) 
        self.forward = My_Button('forwardbutton.png', self.player_w.forward_5_sec)
        self.backwards = My_Button('backwardsbutton.png', self.player_w.backwards_5_sec)
        self.volume_slider = Volume_Slider(self.player_w.player.audio_set_volume)
        self.button_repeat = My_Button('repeatbutton.png', lambda: self.player_w.repeat(self.button_play))
        self.media_slider = Media_Slider(self.player_w.player.set_position, self.player_w.player.is_playing, self.player_w.player.get_time,self.player_w.player.get_length)
        self.volume_icon = My_Button('volume.png', lambda: None)
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

class OP_Exception(Exception):
    pass

class Player_App(App):
    player_pool = list((Player_Window("", ""), Player_Window("", "")))
    
    def __init__(self, path, cover_path, **kwargs):
        #resources.resource_add_path("path to folder where stored")       #<-- uncomment and fill after fetching files from server is done!!!!!!
        self._path = path
        self._cover_path = cover_path
        super(Player_App, self).__init__(**kwargs)
        
        
    def build(self):
        #self._player_window = Player_Window(self._path, self._cover_path)
        self._player_window = Player_App.get_player(self._path, self._cover_path)
        print(self._player_window)
        #change_slider_state(self._player_window.media_slider.change_state, self._player_window.player_w.player.get_position)
        return self._player_window
    
    def on_stop(self):
        self._player_window.player_w.player.stop()
        Player_App.free_player(Player_App, self._player_window)

    @classmethod
    def get_player(cls, path, cover):
        try:
            if Player_App.player_pool == []:
                raise OP_Exception('You already have maximum windows with player open')
            else:
                Player_App.player_pool[0].reset_player(path, cover)
                return Player_App.player_pool.pop(0)
        except OP_Exception as e:
            print(e.args)

    def free_player(cls, p):
        Player_App.player_pool.append(p)


Player_App('test.mp3', '').run()           #uncomment to test
