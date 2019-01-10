import kivy
import sys
sys.path.append('./model/data_base')
import users_data
from kivy.uix.boxlayout import BoxLayout 
kivy.require('1.10.1')

class Sidebar(BoxLayout):
    def __init__(self, *args, **kwargs):
        u = users_data.Users_data()
        self.username = u.get_users('Andrzej')[0][0]
        super(Sidebar, self).__init__(*args, **kwargs)
    def shop(self, instance):
        self.track_list.clear_widgets()
