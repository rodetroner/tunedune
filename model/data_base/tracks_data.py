import data_base

class Tracks_data():
    def __init__(self):
        self.db = data_base.Data_Base()
        self.db.connect_to_data_base()
        self.connection = self.db.get_connection()
        self.cursor = self.db.db_cursor

    def get_tracks(self, track_name = '', authors = list(), tags = list(), id_track = ''):
        if id_track != '':
            self.cursor.execute("select id_track, track_name, durration, track_price, path, track_status, cover_path from track where id_track = %s", (id_track)) 
            return self.cursor.fetchall()
        temp = list()
        rvalue = list()
        track_name = '%' + track_name + '%'
        if authors !=  []:
            for i in authors:
                self.cursor.execute("select id_track, track_name, durration, track_price, path, track_status, cover_path from track join authors_to_tracks on authors_to_tracks.id_track = track.id_track join authors on authors.id_author = authors_to_tracks.id_author where track_name like %s and author.author_name like %s", (track_name, '%' + i + '%'))
                tmp = self.cursor.fetchall()
                for j in tmp:
                    temp.append(j)
        else:
            self.cursor.execute("select id_track, track_name, durration, track_price, path, track_status, cover_path from track where track_name like %s", ('%' + track_name + '%'))
            temp = self.cursor.fetchall()
        if tags != []:
            for i in temp:
                for j in tags:
                    if self.cursor.execute("select id_track from tags join tags_to_tracks on tags.id_tag = tags_to_tracks.id_tag where id_track = %s and tag_name = %s", (i[0], j)):
                        break
                else: rvalue.append(i)
        else: rvalue = temp
        return set(rvalue)

    def get_authors(self, id_track = None):
        if id_track:
            self.cursor.execute("select author_name, id_author, id_user from author where id_author in (select id_author from authors_to_tracks where id_track = %s)", (id_track))
        else:
            self.cursor.execute("select author_name, id_author, id_user from author")
        return self.cursor.fetchall()

    def get_tags(self, id_track = None):
        if id_track:
            self.cursor.execute("select tag_name, id_tag from tags where id_tag in (select id_tag from tags_to_tracks where id_track = %s)", (id_track))
        else:
            self.cursor.execute("select tag_name, id_tag from tags")
        return self.cursor.fetchall()
    
    def add_track(self, track_name, durration, track_price, path, track_status, cover_path):
        if track_name == '' or durration == '' or track_price == '' or path == '' or track_status == '':
            return 0
        else:
            self.connection.begin()
            self.cursor.execute("INSERT INTO track (track_name, durration, track_price, path, track_status, cover_path) VALUES (%s, %s, %s, %s, %s)", (track_name, durration, track_price, path, track_status, cover_path))
            self.connection.commit()
            return 1

    def alter_track(self, id_track, track_name= '', durration= '', track_price= '', path= '', track_status = '',cover_path = ''):
        if track_name == '' and durration == '' and track_price == '' and path == '' and track_status == '':
            return 0
        else:
            self.connection.begin()
            if track_name != '':
                self.cursor.execute("UPDATE track SET track_name = %s WHERE id_track = %s;", (track_name, id_track))
            if durration != '':
                self.cursor.execute("UPDATE track SET durration = %s WHERE id_track = %s;", (durration, id_track))
            if track_price != '':
                self.cursor.execute("UPDATE track SET track_price = %s WHERE id_track = %s;", (track_price, id_track))
            if path != '':
                self.cursor.execute("UPDATE track SET path = %s WHERE id_track = %s;", (path, id_track))
            if track_status != '':
                self.cursor.execute("UPDATE track SET track_status = %s WHERE id_track = %s;", (track_status, id_track))
            if cover_path != '':
                self.cursor.execute("UPDATE track SET cover_path = %s WHERE id_track = %s;", (cover_path, id_track))
            self.connection.commit()
        return 1

    def delete_track(self, id_track):
        if not id_track:
            return 0
        else:
            self.connection.begin()
            self.cursor.execute("DELETE FROM track WHERE id_track = %s", (id_track))
            self.connection.commit()
        return 1

'''#uncoment to test (id may not be right for test)
a = Tracks_data()
print(a.get_tracks())
print(a.add_track(track_name = '', durration = '', track_price = '', path = '', track_status = ''))
print(a.add_track(track_name = 'b', durration = '00:00:01', track_price = 1, path = 'b', track_status = '1'))
print(a.get_tracks())
print(a.alter_track('2', track_name = 'b2'))
print(a.get_tracks())
print(a.delete_track('3'))
print(a.get_tracks())
'''
