import pymysql

from pymysql.connections import Connection
from pymysql.cursors import Cursor
from pymysql.err import DatabaseError

class Data_Base():
    """Singleton class for storing connector to DB.
    """
    class DB:
        """Actual connector class.
        """
        def __init__(self):
            self.connect_to_data_base()
         
        def connect_to_data_base(self):
            try:
                self.connection = Connection(host = '127.0.0.1',
                                             user = 'root',
                                             password = 'tunedunedbpass1!',
                                             database = 'tunedune_db',
                                             port = 3306)
            except DatabaseError:
                print('Error on creating connection')
                return None
            self.db_cursor = Cursor(self.connection)
        
        def disconnect(self):
            if self.connection.open:
                self.close()

    """Instance of connector's class.
    """
    DB_instance = None

    def __init__(self):
        if Data_Base.DB_instance == None:
            Data_Base.DB_instance = Data_Base.DB()
            self.db_cursor = Data_Base.DB_instance.db_cursor

    def get_connection(self):
        """Returns a connection.
        """
        return Data_Base.DB_instance.connection
        
    def connect_to_data_base(self):
        """Initializer of DB connection.
        """
        Data_Base.DB_instance.connect_to_data_base()
        self.db_cursor = Data_Base.DB_instance.db_cursor

    def disconnect(self):
        """Deinitializer of DB connection.
        """
        Data_Base.DB_instance.disconnect()
