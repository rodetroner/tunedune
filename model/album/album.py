import sys

sys.path.append('../data_base')
sys.path.append('../user')
sys.path.append('../track')
sys.path.append('../exceptions')

from albums_data import Albums_data
from track import *
from user import User
from exceptions import Ex_Handler

"""List of schearched albums.
"""
curr_searched_album_list = list()

class Album_Builder(Builder):
    """Part of builder of Albums
    """
    def __init__(self):
        self.ad = Albums_data()
        self.album = Album() 
    
    def set_data(self, data):
        self.album._id_album = data[0]
        self.album._album_name = data[1]
        return self

    def set_authors(self):
        self.album._authors = self.ad.get_authors(self.album._id_album)
        return self

    def set_tags(self):
        self.album._tags = self.ad.get_tags(self.album._id_album)
        return self

    def set_tracks(self):
        a = self.ad.get_tracks_from_album(self.album._id_album)
        self.album._tracks = fetch_album_tracks(a)
        return self

    def get_final(self):
        return self.album

class Album_Builder_Director:
    """Part of albums builder.
    """
    @classmethod
    def cosntruct(cls, data = list()):
        try:
            if len(data) != 2:
                raise Ex_Data()
        except (Ex_Data):
            Ex_Handler.call('Data integriti error')
            return
        return (Album_Builder()
                .set_data(data)
                .set_authors()
                .set_tags()
                .set_tracks()
                .get_final()
               )
class Album:
    """Class for handeling albums informations, and actions like buying.
    """
    def __init__(self):
        self._id_album = None
        self._album_name = None
        self_authors = None
        self._tags = None
        self._tracks = None
        self.curr_track = 0

    def upload(self):
        ad = Albums_data()
        ad.add_album(self, self._album_name, self.album._track)

    def add_track(self, track): #add check for admin and allow to delete and add track to album
        self._tracks.append(track)

    def delete_track(self, track):
        self._tracks.remove(track)

    def get_next_track(track_number = None):
        if track_number:
            self.curr_track = track_number
        else:
            self.curr_track += 1
        if self.curr_track >= len(self._tracks):
            return 0
        else:
            return self._track[self.curr_track]
            
    def buy(self, user, time):
        total_price = 0
        a = Tracks_data()
        for i in self._tracks:
            if a.check_track_for_buy(i.get_track_id, user.login):
                total_price += i.get_track_price()
        if Payment.update_balance(user, total_price):
            for j in self._tracks:
                a.buy_track(j.get_track_id(), user.login, time)
            return 1
        else:
            return 0
        
def search_album(name = '', owner = None, authors = list(), tags = list()):
    """updates searched albums list.
    """
    a = Albums_data().get_albums(name = name, owner = owner, authors = authors, tags = tags)
    for i in a:
        temp = Album_Builder_Director.cosntruct(i)
        if temp == None:
            pass
        else:
            curr_searched_album_list.append(temp)  
    
#search_album()
#print(curr_searched_album_list)
