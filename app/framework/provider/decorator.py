import builtins
import importlib

from . import AbstractProvider


class DecoratorProvider(AbstractProvider):

    def __init__(self, *decorators):
        self.decorators = decorators

    def register(self):
        for decorator in self.decorators:
            module = importlib.import_module(decorator.__module__)
            clazz = str(decorator.__class__.__name__)
            setattr(builtins, clazz, getattr(module, clazz))
