
from abc import ABCMeta


class EventHandler(metaclass=ABCMeta):
    
    @staticmethod
    def on_click(**kwargs):
        pass
    
    @staticmethod
    def on_message(**kwargs):
        pass


class AddressBookEventHandler(EventHandler):

    @staticmethod
    def on_click(**kwargs):
        data = kwargs.get('data')
        return data

