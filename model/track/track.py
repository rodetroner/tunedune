import sys

sys.path.append('../data_base')
sys.path.append('../user')
sys.path.append('../transactions')
sys.path.append('../../mediaplayer')
sys.path.append('../exceptions')

from mediaplayer import Player_App
from tracks_data import Tracks_data
from abc import ABCMeta, abstractmethod
from user import User
from exceptions import Ex_Handler

"""List of tracks currently fetched from data base, updated by functions in module.
"""
curr_searched_track_list = list()

class Builder:
    """Part of builder for Track.
    """
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
    """Part of builder for Track.
    """
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
    """Part of builder for Track.
    """
    @classmethod
    def cosntruct(cls, data = list()):
        """Returns Track object based on data from provided list.

        List should come from module handeling data base.
        """
        try:
            if len(data) != 7:
                raise Ex_Data()
        except (Ex_Data):
            Ex_Handler.call('Data integrity error.')
            return
        return Track_Builder().set_data(data).set_authors().set_tags().get_final()
    

class Track:
    """Class for containing information on track, accessing them.

    Also allows to play particular track adding to playlist/album and buing it.
    Track should be created via Track_Builder_Director class.
    """
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

    def buy(self, user, time):
        total_price = 0
        a = Tracks_data()
        if a.check_track_for_buy(self._id_track, user.login):
            total_price += i.get_track_price()
        if Payment.update_balance(user, total_price):
            a.buy_track(j.get_track_id(), user.login, time)
            return 1
        else:
            return 0
        
    def play_track(self):
        Player_App(self._path, self._cover_path)
    
    def add_to_album(self, album):
        album.add_track(self)

def search_track(name = '', authors = list(), tags = list()):
    """Function that based on given arguments will update list (curr_searched_track_list).
    """
    a = Tracks_data().get_tracks(track_name = name, authors = authors, tags = tags)
    for i in a:
        curr_searched_track_list.append(Track_Builder_Director.cosntruct(i))
    
    
def fetch_album_tracks(album_tracks = list()):
    """Based on list of id track returns list of Track objects

    This should be called from module handeling albums.
    """
    tmp = list()
    rvalue = list()
    for i in album_tracks:
        tmp.append(Tracks_data().get_tracks(id_track = i[0][0]))
    for i in tmp:
        temp = Track_Builder_Director.cosntruct(i[0])
        if temp == None:
            pass
        else:
            rvalue.append(temp)
    return rvalue
    
#uncomment to test   
#search_track()
#print(curr_searched_track_list[0].get_track_name())
