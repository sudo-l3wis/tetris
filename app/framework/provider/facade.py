from . import AbstractProvider


class FacadeProvider(AbstractProvider):

    def __init__(self, *facades):
        self.facades = facades

    def register(self):
        for facade in self.facades:
            facade.register()
