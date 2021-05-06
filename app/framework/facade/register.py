from . import AbstractFacade
from app.framework.singleton import Dispatcher


class RegisterFacade(AbstractFacade):

    def __init__(self):
        super().__init__('register')

    def invoke(self, event, listener):
        """Dispatch the given event.
        :param event The event to watch.
        :param listener The listener to bind.
        """
        Dispatcher().register(event, listener)
