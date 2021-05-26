import yaml

from . installer import AbstractInstaller


class ScoreConfig(AbstractInstaller):
    def install(self, config):
        with open('./config/score.yml') as f:
            config.put('score', yaml.safe_load(f))
