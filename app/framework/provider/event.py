from . import AbstractProvider
from app.singleton import Config

class EventProvider(AbstractProvider):

    def register(self):
        events = Config().get('events')
        for event, listeners in events.items():
            for listener in listeners:
                Dispatcher().register(event, listener)
