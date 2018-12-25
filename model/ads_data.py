import data_base

class Ads_data():
    def __init__(self):
        self.db = data_base.Data_Base()
        self.db.connect_to_data_base()
        self.connection = self.db.get_connection()
        self.cursor = self.db.db_cursor

    def get_ads(self, ads_type = '', ad_provider = ''):
        self.cursor.execute("select ad_name, ad_path, ad_reward from ads where ads_type like %s and ad_provider like %s", ('%' + ads_type + '%', '%' + ad_provider + '%'))
        return self.cursor.fetchall()
    
    def add_ad(self, ad_name, ad_provider, ad_path, ad_reward, ads_type):
        if ad_name == '' or ad_provider == '' or ad_path == '' or ad_reward == '' or ads_type == '':
            return 0
        else:
            self.connection.begin()
            self.cursor.execute("INSERT INTO ads (ad_name, ad_provider, ad_path, ad_reward, ads_type) VALUES (%s, %s, %s, %s, %s)", (ad_name, ad_provider, ad_path, ad_reward, ads_type))
            self.connection.commit()
            return 1

    def alter_ad(self, id_ad, ad_name= '', ad_provider= '', ad_reward= '', ad_path= '', ads_type = ''):
        if ad_name == '' and ad_provider == '' and ad_reward == '' and ad_path == '' and ads_type == '':
            return 0
        else:
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
            self.connection.commit()
        return 1

    def delete_ad(self, id_ad):
        if id_ad == None:
            return 0
        else:
            self.connection.begin()
            self.cursor.execute("DELETE FROM ads WHERE id_ad = %s", (id_ad))
            self.connection.commit()
        return 1

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
