import yaml

from . installer import AbstractInstaller


class SpriteConfig(AbstractInstaller):
    def install(self, config):
        with open('./config/sprites.yml') as f:
            config.put('sprites', yaml.safe_load(f))
