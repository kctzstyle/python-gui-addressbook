
from abc import ABCMeta


class EventHandler(metaclass=ABCMeta):
    
    @staticmethod
    def on_click(e, **kwargs):
        pass
    
    @staticmethod
    def on_message(e, **kwargs):
        pass


class AddressBookEventHandler(EventHandler):

    @staticmethod
    def on_click(e, **kwargs):
        data = kwargs.get('data')
        return data

