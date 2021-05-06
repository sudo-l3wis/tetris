import yaml

from . installer import AbstractInstaller


class DisplayConfig(AbstractInstaller):
    def install(self, config):
        with open('./config/display.yml') as f:
            config.put('display', yaml.safe_load(f))
