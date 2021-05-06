from app.framework.singleton import Config
from . import AbstractProvider


class ConfigProvider(AbstractProvider):

    def __init__(self, *installers):
        self.installers = installers

    def register(self):
        """Load all application configs.
        Iterate over & apply the injected config property
        installers.
        """
        for installer in self.installers:
            installer.install(Config())
