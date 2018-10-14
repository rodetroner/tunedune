import vlc
import time

class Player:
    def __init__(self):
        self.__instance = vlc.Instance()
        self.__media = False
        self.__player = False
    
    def play_track(self, path):
        self.__player = self.__instance.media_player_new() #creating instance of MP
        self.__media = self.__instance.media_new(path)     #create instance of media
        self.__player.set_media(self.__media)              #load file into player
        self.__player.play()                               #play file
        

'''''test
a = Player()
a.play_track('test.mp3')
'''''
