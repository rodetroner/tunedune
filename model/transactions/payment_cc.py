import sys
sys.path.append('../data_base')
from users_data import Users_data
from payments_data import Payments_data
from datetime import date

class Payment_CC:
    @classmethod
    def check_balance(cls, login):
        return Users_data().get_payment_cc(login)

    @classmethod
    def pay_cc(cls, login, payment_type, payment_destination):
        Payments_data.schedule_payment(login, Payment_CC.check_balance(login), payment_type, payment_destination = payment_destination)
        Users_data().clear_cc_payment(login)


    @classmethod
    def check_schedule(self, login = '', id_payment = ''):
        return Payments_data().check_schedule(login = login, id_payment = id_payment)

    @classmethod
    def show_all():
        return Payments_data().check_schedule(show_all = True)

    @classmethod
    def show_not_realized():
        return Payments_data().check_schedule(show_not_realized = True)
        
    @classmethod
    def cancel_payment(cls, id_payment):
        Payments_data.cancel(cls, id_payment)

    @classmethod
    def mark_realized(id_payment, date = date.today()):
        Payments_data.mark_realized(id_payment, date)
    
            
