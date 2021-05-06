from app.framework.singleton import Config
from . import AbstractFacade


class ConfigFacade(AbstractFacade):

    def __init__(self):
        super().__init__('config')

    def invoke(self, attr=False, value=False):
        if attr:
            if value:
                return Config().put(attr, value)
            return Config().get(attr)
        return Config()
