import kivy
import sys
sys.path.append('./model')
sys.path.append('./mediaplayer_d')
sys.path.append('./model/exceptions_d')
sys.path.append('./model/user_d')
import user_d.user
import track_d.track
from kivy.uix.screenmanager import Screen

kivy.require('1.10.1')

class MainScreen(Screen):
    def logOut(self, instance, *args):
        user_d.user.User.logout(self.login_screen.current_session)
        print(self.login_screen.current_session)

    def search(self, instance, *args):
        track_d.track.search_track(name ='turystyczna_piosenka')
        print(track_d.track.curr_searched_track_list)
