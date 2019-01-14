class PA_Exception(Exception):
    """For Player_App exceptions.
    """
    pass

class OP_Exception(Exception):
    """For object pool exceptions.
    """
    pass

class Ex_Data(Exception):
    """For data exceptions.
    """
    pass

class Ex_Handler:
    """Class for spqwning pop up about exception occuring.
    """
    @classmethod
    def call(cls, string):
        print(string)

