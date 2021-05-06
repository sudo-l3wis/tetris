import builtins

from abc import ABCMeta, abstractmethod


class AbstractFacade(metaclass=ABCMeta):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def invoke(self, *args, **kwargs):
        pass

    def register(self):
        setattr(builtins, self.name, self.invoke)
