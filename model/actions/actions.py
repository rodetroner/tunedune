import sys

sys.path.append('../data_base')
sys.path.append('../user')
sys.path.append('../../mediaplayer')

from ads_data import Ads_data
from user import User
from mediaplayer import Player_App

list_of_schearched_ads = list()
list_of_watched_ads = list()

class Promotional_action:
    def __init__(self, data):
        self.name = data[0]
        self.path = data[1]
        self.reward = data[2]
        self.provider = data[3]
        self.type = data[4]

    def block_action(self):
        if not self.check_if_watched():
            list_of_watched_ads.append(self.path)

    def check_if_watched(self):
        if self.path in list_of_watched_ads:
            return 1
        else:
            return 0

    def reward_user(self, user):
        user.alter_user(balance_change = reward)

    def run_ad(self):
        pass
    
class Image_advertisment(Promotional_action):
    def run_ad(self):
        Player_App('', self.path) #to do: consider adding dummy path for mediaplayer

class Sound_advertisment(Promotional_action):
    def run_ad(self):
        Player_App(self.path, '')

class Ad_factory:
    @classmethod
    def make_ads(cls, data):
        for i in data:
            targetclass = Ads_data().get_ad_type(i[4])[0][0].capitalize()
            tmp = globals()[targetclass](i)
            if tmp.check_if_watched():
               return
            else:
                list_of_schearched_ads.append(tmp)
                
def search_ads(ads_type = '', ad_provider = ''):
    list_of_schearched_ads = list()
    data = Ads_data().get_ads(ads_type = ads_type, ad_provider = ad_provider)
    Ad_factory.make_ads(data)
    
#uncomment to test    
#search_ads()
#print(type(list_of_schearched_ads[0]))
