import vlc

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
