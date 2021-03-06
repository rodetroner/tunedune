import vlc
import kivy

kivy.require('1.10.1')

from kivy.clock import Clock

class Player:
    """Class for handeling operations on mediaplayer.
    In this class the instance of player is created based on media from given
    path. It also defines methods to interact with it that may be passed to
    buttons.
    """
    _observers = set()
    
    def __init__(self, path):
        self.__instance = vlc.Instance()
        self.__media = None
        self.player = None
        self.__path = path
        
    def observe(self, inform):
        Player._observers.add(inform)
        
    def inform(self):
        for i in Player._observers:
            i()

    def start_clock(self):
        """Starts the dispatcher for updating slider's position.
        """
        Clock.schedule_interval(self.media_watcher, 0.1)

    def media_watcher(self, delta_time):
        if self.player.get_state() == vlc.State.Ended:
            self.inform()
        
    def play_track(self):
        """Sets media for mediaplayer based on path provided in __init__.
        """
        self.player = self.__instance.media_player_new()      #creating instance of MP
        self.__media = self.__instance.media_new(self.__path)   #create instance of media
        self.player.set_media(self.__media)                   #load file into player
        
    def forward_5_sec(self):
        length = self.player.get_length()
        if self.player.get_time() + 5000 > length:
            self.player.set_position(10)
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
        self.player.set_position(0)
        self.player.set_media(self.__media)
        self.player.set_position(0)
        self.player.play()
        pb.version = 1
        pb.source = pb.path2
        pb.function = pb.function2
