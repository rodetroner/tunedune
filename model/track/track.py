import sys
sys.path.append('../data_base')
sys.path.append('../../mediaplayer')
#from mediaplayer import Player_Window
from argon2 import PasswordHasher
from tracks_data import Tracks_data
from abc import ABCMeta, abstractmethod

curr_searched_track_list = list()

class Builder:
    __metaclass__ = ABCMeta

    @abstractmethod
    def set_data(self, data):
        pass

    @abstractmethod
    def set_authors(self):
        pass

    @abstractmethod
    def set_tags(self):
        pass

class Track_Builder(Builder):
    def __init__(self):
        self.td = Tracks_data()
        self.track = Track() 
    
    def set_data(self, data):
        self.track._id_track = data[0]
        self.track._track_name = data[1]
        self.track._durration = data[2]
        self.track._track_price = data[3]
        self.track._path = data[4]
        self.track._track_status = data[5]
        self.track._cover_path = data[6]
        return self

    def set_authors(self):
        self.track._authors = self.td.get_authors(self.track._id_track)
        return self

    def set_tags(self):
        self.track._tags = self.td.get_tags(self.track._id_track)
        return self

    def get_final(self):
        return self.track

class Track_Builder_Director:
    @classmethod
    def cosntruct(cls, data = list()):
        return Track_Builder().set_data(data).set_authors().set_tags().get_final()
    

class Track:
    def __init__(self):
        self._id_track = None
        self._track_name = None
        self._durration = None
        self._track_price = None
        self._path = None
        self._track_status = None
        self._cover_path = None
        self._authors = None
        self._tags = None
        
    def get_track_id(self):
        return self._id_track

    def get_track_name(self):
        return self._track_name

    def get_track_durration(self):
        return self._durration

    def get_track_price(self):
        return self._track_price

    def get_track_path(self):
        return self._path

    def get_track_status(self):
        return self._track_status
    
    def get_track_cover(self):
        return self._cover_path

    def get_authors(self):
        return self._authors

    def get_tags(self):
        return self._tags
    
    #def play_track(self):
    #    mediaplayer.Player_Window(self._path, self._cover_path)
    #do that in mediaplayer with observer or smthing

    #def add_to_album(self):

def search_track(name = '', authors = list(), tags = list()):
    a = Tracks_data().get_tracks(track_name = name, authors = authors, tags = tags)
    for i in a:
        curr_searched_track_list.append(Track_Builder_Director.cosntruct(i))

#uncomment to test   
#search_track()
#print(curr_searched_track_list[0].get_track_id())
