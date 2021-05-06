from abc import ABCMeta, abstractmethod


class AbstractProvider(metaclass=ABCMeta):

    @abstractmethod
    def register(self):
        pass
