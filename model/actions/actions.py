import sys

sys.path.append('../data_base')
sys.path.append('../user')
sys.path.append('../../mediaplayer')
sys.path.append('../exceptions')

from ads_data import Ads_data
from user import User
from mediaplayer import Player_App
from exceptions import Ex_Handler

"""Global lists for storing ads.
"""
list_of_schearched_ads = list()
list_of_watched_ads = list()

class Promotional_action:
    """Class for representation of ads in app.
    """
    def __init__(self, data):
        """Argument is a iterable structure, as it is fetched from database like this.
        """
        try:
            if len(data) != 5:
                raise Ex_Data()
        except (Ex_Data):
            Ex_Handler.call('Data integrity error')
            return
        self.name = data[0]
        self.path = data[1]
        self.reward = data[2]
        self.provider = data[3]
        self.type = data[4]

    def block_action(self):
        """Ads actions path to global list of used ads (list_of_watched_ads).
        """
        if not self.check_if_watched():
            list_of_watched_ads.append(self.path)

    def check_if_watched(self):
        """Checks if add in list_of_watched_ads.
        """
        if self.path in list_of_watched_ads:
            return 1
        else:
            return 0

    def reward_user(self, user):
        """Rewards uesr for action.
        """
        user.alter_user(balance_change = reward)

    def run_ad(self):
        pass
    
class Image_advertisment(Promotional_action):
    """Clase implementing run add for specyfic type of ad.
    """
    def run_ad(self):
        Player_App('', self.path) #to do: consider adding dummy path for mediaplayer

class Sound_advertisment(Promotional_action):
    """Clase implementing run add for specyfic type of ad.
    """
    def run_ad(self):
        Player_App(self.path, '')

class Ad_factory:
    """Factory creating specyfic classes for specyfic ads and adds them to searched list.
    """
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
    """Function for updating search list.
    """
    list_of_schearched_ads = list()
    data = Ads_data().get_ads(ads_type = ads_type, ad_provider = ad_provider)
    Ad_factory.make_ads(data)
    
#uncomment to test    
#search_ads()
#print(type(list_of_schearched_ads[0]))
