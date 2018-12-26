import data_base
import datetime

class Tracks_data():
    def __init__(self):
        self.db = data_base.Data_Base()
        self.db.connect_to_data_base()
        self.connection = self.db.get_connection()
        self.cursor = self.db.db_cursor

    def check_schedule(self, id_user = '', id_payment = '', show_all = False, show_not_realized = False):
        if id_user != '':
            self.cursor.execute("select * from payments where id_payment = %s", (id_payment)) 
            return self.cursor.fetchall()
        if id_payment != '':
            self.cursor.execute("select * from payments where id_user = %s", (id_user)) 
            return self.cursor.fetchall()
        if show_all:
            self.cursor.execute("select * from payments")
            return self.cursor.fetchall()
        if show_not_realized:
            self.cursor.execute("select * from payments where payment_status = 0")
            return self.cursor.fetchall()
        return 0
        
    def schedule_payment(self, id_user, value, payment_type, payment_destination = '', date_of_order = datetime.date.today()):
        self.connection.begin()
        self.cursor.execute("INSERT INTO payments (id_user, payment_value, id_payment_type, payment_destination, date_of_order) VALUES (%s, %s, %s, %s, %s)", (id_user, value, payment_type, payment_destination, date_of_order))
        self.connection.commit()
        return 1

    def cancel(self, id_payment):
        self.connection.begin()
        self.cursor.execute("DELETE FROM payments WHERE id_payment = %s", (id_payment))
        self.connection.commit()
        return 1

'''#uncoment to test (id may not be right for test)
a = Tracks_data()
print(a.check_schedule(show_all = True))
print(a.schedule_payment(1, 1, 1))
print(a.check_schedule(show_all = True))
print(a.check_schedule(id_user = '1'))
print(a.cancel('1'))
print(a.check_schedule(show_all = True))
'''
