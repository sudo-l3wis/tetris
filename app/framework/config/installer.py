from abc import ABCMeta, abstractmethod


class AbstractInstaller(metaclass=ABCMeta):
    @abstractmethod
    def install(self, config):
        pass
