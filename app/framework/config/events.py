import yaml

from . installer import AbstractInstaller


class EventConfig(AbstractInstaller):
    def install(self, config):
        with open('./config/events.yml') as f:
            config.put('events', yaml.safe_load(f))
