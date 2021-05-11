from . import AbstractFacade
from app.framework.singleton import Dispatcher


class EmitFacade(AbstractFacade):

    def __init__(self):
        super().__init__('emit')

    def invoke(self, event, payload):
        """Dispatch the given event.
        :param event: The event to dispatch.
        :param: payload: The event data to process.
        :return: The result of the event.
        """
        return Dispatcher().dispatch(event, payload)
