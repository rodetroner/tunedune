import data_base
import datetime

class Paymentss_data():
    """Class for handeling operations on data regarding payments.
    """
    def __init__(self):
        self.db = data_base.Data_Base()
        self.db.connect_to_data_base()
        self.connection = self.db.get_connection()
        self.cursor = self.db.db_cursor

    def check_schedule(self, login = '', id_payment = '', show_all = False, show_not_realized = False):
        """Returns datas needed for creation of objects representing payments as a list
        """
        if login != '':
            self.cursor.execute("select * from payments where id_payment = %s", (id_payment)) 
            return self.cursor.fetchall()
        if id_payment != '':
            self.cursor.execute("select * from payments where id user = (select id_user from users where login = %s)",
                                (login)
                                ) 
            return self.cursor.fetchall()
        if show_all:
            self.cursor.execute("select * from payments")
            return self.cursor.fetchall()
        if show_not_realized:
            self.cursor.execute("select * from payments where payment_status = 0")
            return self.cursor.fetchall()
        return 0
        
    def schedule_payment(self, login, value, payment_type, payment_destination = '', date_of_order = datetime.date.today()):
        """Inserts to data base record widh data regarding new payment.
        """
        self.connection.begin()
        self.cursor.execute("INSERT INTO payments \
                            (id_user, payment_value, id_payment_type, payment_destination, date_of_order) \
                            VALUES ((select id_user from users where login = %s), %s, %s, %s, %s)",
                            (login, value, payment_type, payment_destination, date_of_order)
                            )
        self.connection.commit()
        return 1

    def cancel(self, id_payment):
        """Removes data from data base of payment with provided id.
        """
        self.connection.begin()
        self.cursor.execute("DELETE FROM payments WHERE id_payment = %s", (id_payment))
        self.connection.commit()
        return 1

    def mark_realized(id_payment, date):
        """Changes status of payment and inserts date of realization.
        """
        self.connection.begin()
        self.cursor.execute("UPDATE payments SET date_of_realization = %s, payment_status = 1 WHERE id_payment = %s;",
                            (date, id_payment)
                            )
        self.connection.commit()
        
'''#uncoment to test (id may not be right for test)
a = Paymentss_data()
print(a.check_schedule(show_all = True))
print(a.schedule_payment(1, 1, 1))
print(a.check_schedule(show_all = True))
print(a.check_schedule(id_user = '1'))
print(a.cancel('1'))
print(a.check_schedule(show_all = True))
'''
