from abc import ABCMeta, abstractmethod

class State(metaclass=ABCMeta):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def update(self, delta):
        pass

    @abstractmethod
    def render(self, surface):
        pass
