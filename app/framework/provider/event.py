from . import AbstractProvider

class EventProvider(AbstractProvider):

    def __init__(self, config, dipatcher):
        self.config = config
        self.dispatcher = dipatcher

    def register(self):
        events = self.config.get('events')
        for event, listeners in events.items():
            for listener in listeners:
                self.dispatcher.register(event, listener)
