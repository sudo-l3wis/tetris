import pygame

from abc import ABCMeta, abstractmethod
from app.entity.components import Mouse

class State(metaclass=ABCMeta):

    def __init__(self):
        self.size = (config('display.width'), config('display.height'))
        self.component_surface = pygame.Surface(self.size, flags=pygame.SRCALPHA)
        self.components = [Mouse()]

    def add_component(self, component):
        self.components.insert(0, component)

    @abstractmethod
    def start(self):
        for component in self.components:
            component.on_mount()

    @abstractmethod
    def update(self, delta):
        for component in self.components:
            component.update(delta)


    @abstractmethod
    def render(self, surface):
        pass

    @abstractmethod
    def on_key(self, key):
        pass

    @abstractmethod    
    def restart(self):
        pass

    def render_ui(self, surface):
        self.component_surface.fill((0, 0, 0, 0))
        for component in self.components:
            component.render(self.component_surface)

        surface.blit(self.component_surface, (0, 0))
