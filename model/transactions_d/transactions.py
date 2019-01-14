import sys

sys.path.append('../user_d')

from user import User
from abc import ABCMeta, abstractmethod

class Transaction(ABCMeta):
    """Base class for handeling users balance.
    """
    @abstractmethod
    def dekorator(fun):
        pass
    
    @classmethod
    @dekorator
    def update_balance(user, value):
        user.alter_user(balance = value)

class Payment(Transaction):
    """Class for balance decresing opperations. 
    """
    def dekorator(fun):
        def wraper(user, value):
            if user.balance < value:
                return 0
            value = -1 * value
            fun(user, value)
            return 1

class Top_up(Transaction):
    """Class for balance incresing opperations through external means. 
    """
    def dekorator(fun):
        def wraper(user, value):
            #validate code passed as value, not present in system though
            fun(user, value)
            return 1


class Freebies(Transaction):
    """Class for balance incresing opperations through internal means.
    """
    def dekorator(fun):
        def wraper(user, value):
            #validate code passed as value, not present in system though
            fun(user, value)
            return 1
        
