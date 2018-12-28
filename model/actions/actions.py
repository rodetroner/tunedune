import sys
sys.path.append('../data_base')
sys.path.append('../user')
from ads_data import Ads_data
from user import User

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
        if not self.check_if_watched()
            list_of_watched_ads.append(self.path)

    def check_if_watched(self):
        if self.path in list_of_watched_ads.append:
            return 1
        else:
            return 0

    def reward_user(self, user):
        user.alter_user(balance_change = reward)

    def run_add(self):
        pass
    

    

    
