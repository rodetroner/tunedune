import sys
sys.path.append('../user')
from user import User
from abc import ABCMeta, abstractmethod

class Transaction(ABCMeta): 
    @abstractmethod
    def dekorator(fun):
        pass
    
    @classmethod
    @dekorator
    def update_balance(user, value):
        user.alter_user(balance = value)

class Payment(Transaction):
    def dekorator(fun):
        def wraper(user, value):
            if user.balance < value:
                return 0
            value = -1 * value
            fun(user, value)
            return 1

class Top_up(Transaction):
    def dekorator(fun):
        def wraper(user, value):
            #validate code passed as value, not present in system though
            fun(user, value)
            return 1


class Freebies(Transaction):
    def dekorator(fun):
        def wraper(user, value):
            #validate code passed as value, not present in system though
            fun(user, value)
            return 1
        
