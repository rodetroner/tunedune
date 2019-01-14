import kivy

kivy.require('1.10.1')

from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

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
    def call(cls, s):
        content=BoxLayout(orientation='vertical')
        btn = Button(text='Close')
        l = Label(text=s)
        content.add_widget(l)
        content.add_widget(btn)
        popup = Popup(title='Error!', content = content)
        btn.bind(on_press=popup.dismiss)
        popup.open()



    




