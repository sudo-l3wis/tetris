from app.framework.singleton import App
from . import AbstractFacade


class AppFacade(AbstractFacade):

    def __init__(self):
        super().__init__('app')

    def invoke(self, key=False):
        if key:
            return App().get(key)
        return App()
