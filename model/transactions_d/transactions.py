import sys

sys.path.append('../user_d')

from user import User

class Transaction:
    """Base class for handeling users balance.
    """
    def __init__(self):
        pass
    
    def dekorator(fun):
        pass
    
    @dekorator
    def update_balance(user, value):
        user.alter_user(balance = value)

class Payment(Transaction):
    """Class for balance decresing opperations. 
    """
    def dekorator(fun):
        def wraper(self, user, value):
            if float(user.balance) < value:
                return 0
            value = -1 * value
            fun(user, value)
            return 1
        return wraper

    @dekorator
    def update_balance(user, value):
        user.alter_user(balance = value)

class Top_up(Transaction):
    """Class for balance incresing opperations through external means. 
    """
    def dekorator(fun):
        def wraper(self, user, value):
            #validate code passed as value, not present in system though
            fun(user, value)
            return 1
        return wraper
    
    @dekorator
    def update_balance(user, value):
        user.alter_user(balance = value)
        
class Freebies(Transaction):
    """Class for balance incresing opperations through internal means.
    """
    def dekorator(fun):
        def wraper(self, user, value):
            #validate code passed as value, not present in system though
            fun(user, value)
            return 1
        return wraper
        
    @dekorator
    def update_balance(user, value):
        user.alter_user(balance = value)
