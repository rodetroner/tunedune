import pymysql
from pymysql.connections import Connection
from pymysql.err import DatabaseError

class My_Connection(Connection):
    def __init__(self):
        try:
            super(My_Connection, self).__init__(host = '127.0.0.1', user = 'root', password = 'tunedunedbpass1!', database = 'tunedune_db', port = 3306)
        except DatabaseError:
            print('Error on creating connection')
            return None

    def close_connection():
        self.close()
        
#My_Connection()
