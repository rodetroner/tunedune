import dbase
import sys

sys.path.append('../exceptions')

from pymysql.err import MySQLError
from exceptions import Ex_Handler

class Ads_data():
    """Class for handeling operations on data regarding ads.
    """
    def __init__(self):
        self.db = data_base.Data_Base()
        self.db.connect_to_data_base()
        self.connection = self.db.get_connection()
        self.cursor = self.db.db_cursor

    def get_ads(self, ads_type = '', ad_provider = ''):
        """Returns datas needed for creation of objects representing ads as a list
        """
        try:
            self.cursor.execute("select ad_name, ad_path, ad_reward, ad_provider, ads_type from ads \
                                where ads_type like %s and ad_provider like %s",
                                ('%' + ads_type + '%', '%' + ad_provider + '%')
                                )
        except (MySQLError):
            Ex_Handler.call('Data base error')
            return
        else:
            return self.cursor.fetchall()
    
    def add_ad(self, ad_name, ad_provider, ad_path, ad_reward, ads_type):
        """Inserts to data base record widh data regarding new ad.
        """
        if ad_name == '' or ad_provider == '' or ad_path == '' or ad_reward == '' or ads_type == '':
            return 0
        else:
            try:
                self.connection.begin()
                self.cursor.execute("INSERT INTO ads (ad_name, ad_provider, ad_path, ad_reward, ads_type) \
                                    VALUES (%s, %s, %s, %s, %s)",
                                    (ad_name, ad_provider, ad_path, ad_reward, ads_type)
                                    )
            except (MySQLError):
                Ex_Handler.call('Data base error')
                return
            else:
                self.connection.commit()
                return 1

    def alter_ad(self, id_ad, ad_name= '', ad_provider= '', ad_reward= '', ad_path= '', ads_type = ''):
        """Changes data in database, regarding ad.
        """
        if ad_name == '' and ad_provider == '' and ad_reward == '' and ad_path == '' and ads_type == '':
            return 0
        else:
            try:
                self.connection.begin()
                if ad_name != '':
                    self.cursor.execute("UPDATE ads SET ad_name = %s WHERE id_ad = %s;", (ad_name, id_ad))
                if ad_provider != '':
                    self.cursor.execute("UPDATE ads SET ad_provider = %s WHERE id_ad = %s;", (ad_provider, id_ad))
                if ad_reward != '':
                    self.cursor.execute("UPDATE ads SET ad_reward = %s WHERE id_ad = %s;", (ad_reward, id_ad))
                if ad_path != '':
                    self.cursor.execute("UPDATE ads SET ad_path = %s WHERE id_ad = %s;", (ad_path, id_ad))
                if ads_type != '':
                    self.cursor.execute("UPDATE ads SET ads_type = %s WHERE id_ad = %s;", (ads_type, id_ad))
            except (MySQLError):
                Ex_Handler.call('Data base error')
                return
            else:
                self.connection.commit()
                return 1

    def delete_ad(self, id_ad):
        """Removes data from data base of ad with provided id.
        """
        if id_ad == None:
            return 0
        else:
            try:
                self.connection.begin()
                self.cursor.execute("DELETE FROM ads WHERE id_ad = %s", (id_ad))
            except (MySQLError):
                Ex_Handler.call('Data base error')
                return
            else:
                self.connection.commit()
                return 1

    def get_ad_type(self, type_id):
        """Fetches from data base type of ad as a list.
        """
        try:
            self.cursor.execute("select ads_type_name from ads_types where id_ads_type = %s", (type_id))
        except (MySQLError):
            Ex_Handler.call('Data base error')
            return
        else:
            return self.cursor.fetchall()

'''#uncoment to test (id may not be right for test)
a = Ads_data()
print(a.get_ads())
print(a.add_ad(ad_name = '', ad_provider = '', ad_reward = '', ad_path = '', ads_type = ''))
print(a.add_ad(ad_name = 'b', ad_provider = 'q', ad_reward = '1', ad_path = 'b', ads_type = '1'))
print(a.get_ads())
print(a.alter_ad('2', ad_name = 'b2'))
print(a.get_ads())
print(a.delete_ad('2'))
print(a.get_ads())
'''
