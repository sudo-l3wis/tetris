from . import MetaSingleton
from app.framework.service.pipeline import Pipeline


class Dispatcher(metaclass=MetaSingleton):

    def __init__(self):
        self.listeners = {}

    def register(self, event, listener):
        """Register an event listener.
        :param event: The event to watch.
        :param listener: The listener to bind to the given event.
        """
        if event in self.listeners:
            self.listeners.append(listener)
        else:
            self.listeners[event] = [listener]

    def dispatch(self, event, payload = []):
        """Dispatch the given event.
        Dispatch the event and invoke all attached listeners with
        the given payload.
        :param event: The event to dispatch.
        :param payload: The data to pass to each listener.
        """
        listeners = self.__get_listeners(event)
        
        return Pipeline().send(payload).through(listeners).then(lambda i: i)

    def __get_listeners(self, event):
        """Get event listeners for the given event.
        :param event: The event to fetch listeners for.
        """
        if event in self.listeners:
            return self.listeners[event]

        return []
