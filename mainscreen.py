import kivy
import sys
sys.path.append('./model')
sys.path.append('./model/data_base')
sys.path.append('./model/exceptions_d')
sys.path.append('./model/transactions_d')
sys.path.append('./mediaplayer_d')
sys.path.append('./model/user_d')
import user_d.user
import track_d.track
import album_d.album

from kivy.uix.screenmanager import Screen

kivy.require('1.10.1')

class MainScreen(Screen):
    def logOut(self, instance, *args):
        user_d.user.User.logout(self.login_screen.current_session)
        print(self.login_screen.current_session)

    def clearSearchTracks(self, instance, *args):
        if self.search_tracks_field.text == 'Search tracks...':
            self.search_tracks_field.text = ''

    def clearSearchAlbums(self, instance, *args):
        if self.search_albums_field.text == 'Search albums...':
            self.search_albums_field.text = ''

    def searchTracks(self, instance, *args):
        track_d.track.search_track(name=self.search_tracks_field.text)
        print(track_d.track.curr_searched_track_list)

    def searchAlbums(self, instance, *args):
        album_d.album.search_album(name=self.search_albums_field.text)
        print(album_d.album.curr_searched_album_list)
