import data_base
import tracks_data

class Albums_data():
    def __init__(self):
        self.db = data_base.Data_Base()
        self.db.connect_to_data_base()
        self.connection = self.db.get_connection()
        self.cursor = self.db.db_cursor

    def get_albums(self, name = '', owner = None, authors = list(), tags = list(), id_album = ''):
        if owner != None:
            self.cursor.execute("select id_album, album_name, owner from albums where album_name \
                                like %s and owner = %s",
                                ('%' + name + '%', owner)
                                )
            return self.cursor.fetchall()
        if id_album != '':
            self.cursor.execute("select id_album, album_name, owner from albums from albums where id_album = %s",
                                (id_album)
                                ) 
            return self.cursor.fetchall()
        temp = list()
        rvalue = list()
        name = '%' + name + '%'
        if authors !=  []:
            self.cursor.execute("select id_album, album_name, owner from albums where album_name like %s",
                                ('%' + name + '%')
                                )
            t = self.cursor.fetchall()
            for o in t:
                for i in authors:
                    if not self.cursor.execute("select id_album from authors_to_albums \
                                                join authors on authors.id_author = authors_to_albums.id_author \
                                                where id_album = %s and author.author_name like %s",
                                               (o[0], '%' + i + '%')):
                        break
                else:
                    temp.append(o)
        else:
            self.cursor.execute("select id_album, album_name, owner from albums where album_name like %s",
                                ('%' + name + '%')
                                )
            temp = self.cursor.fetchall()
        if tags != []:
            for i in temp:
                for j in tags:
                    if self.cursor.execute("select id_album, album_name, owner from tags \
                                            join tags_to_albums on tags.id_tag = tags_to_albums.id_tag \
                                            where id_album = %s and tag_name = %s"
                                           , (i[0], j)
                                           ):
                        break
                else: rvalue.append(i)
        else: rvalue = temp
        return set(rvalue)
    
    def add_album(self, album_name, owner = None, tracks_for_album = list()):
        self.connection.begin()
        self.cursor.execute("INSERT INTO albums (album_name, owner) VALUES (%s, %s)", (album_name, owner))
        self.connection.commit()
        self.cursor.execute("select LAST_INSERT_ID()")
        self.add_tracks_to_album(self.cursor.fetchall(), tracks_for_album)
        return 1

    def alter_album(self, id_album, album_name= '', new_owner = None):
        self.connection.begin()
        if new_owner:
            if album_name != '':
                self.cursor.execute("UPDATE album SET album_name = %s owner = %s WHERE id_album = %s;"
                                    , (album_name, owner, id_album)
                                    )
            else:
                self.cursor.execute("UPDATE album SET owner = %s WHERE id_album = %s;", (owner, id_album))
        else:
            self.cursor.execute("UPDATE album SET album_name = %s WHERE id_album = %s;", (album_name, id_album))
        self.connection.commit()
        return 1

    def delete_album(self, id_album):
        if not id_album:
            return 0
        else:
            self.delete_track_from_album(id_album, all_tracks = True)
            self.connection.begin()
            self.cursor.execute("DELETE FROM albums WHERE id_album = %s", (id_album))
            self.connection.commit()
        return 1

    def delete_track_from_album(self, id_album, track_id_list = list(), all_tracks = False):
        if all_tracks:
            self.connection.begin()
            self.cursor.execute("DELETE FROM albums WHERE id_album = %s", (id_album))
            self.connection.commit()
        else:
            self.connection.begin()
            for i in track_id_list:
                self.cursor.execute("DELETE FROM tracks_to_albums WHERE id_album = %s and id_track = %s",
                                    (id_album[0], i)
                                    )
            self.connection.commit()

    def add_tracks_to_album(self, id_album, track_id_list = list()):
        if id_album == []:
            return
        self.connection.begin()
        for i in track_id_list:
            self.cursor.execute("INSERT INTO tracks_to_albums (id_album, id_track) VALUES (%s, %s)", (id_album[0], i))
        self.connection.commit()

    def get_tracks_from_album(self, id_album):
        tmp = list()
        self.cursor.execute("select id_track FROM tracks_to_albums WHERE id_album = %s", (id_album))
        a = self.cursor.fetchall()
        for i in a:
            tmp.append(tracks_data.Tracks_data().get_tracks(id_track = i[0]))
        return tmp

    def get_authors(self, id_album = None):
        if id_album:
            self.cursor.execute("select author_name, id_author, id_user from author \
                                where id_author in (select id_author from authors_to_albums where id_album = %s)",
                                (id_album)
                                )
        else:
            self.cursor.execute("select author_name, id_author, id_user from author")
        return self.cursor.fetchall()

    def get_tags(self, id_album = None):
        if id_album:
            self.cursor.execute("select tag_name, id_tag from tags where id_tag in \
                                (select id_tag from tags_to_albums where id_album = %s)",
                                (id_album)
                                )
        else:
            self.cursor.execute("select tag_name, id_tag from tags")
        return self.cursor.fetchall()

'''#uncoment to test (id may not be right for test)
a = Albums_data()
print(a.add_album('a'))
print(a.add_album('b', owner = '1'))
print(a.get_albums(name = 'a'))
print(a.delete_album('2'))
print(a.add_album('a', tracks_for_album = [1, 2]))
print(a.delete_track_from_album([27], track_id_list = [2]))
print(a.get_tracks_from_album([26]))
'''
