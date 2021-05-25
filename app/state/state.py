import pygame

from abc import ABCMeta, abstractmethod
from app.entity.components import Mouse


class State(metaclass=ABCMeta):

    def __init__(self):
        w = config('display.width')
        h = config('display.height')
        conf = config('sprites.pieces.B')
        block = config('display.grid.block')

        self.size = (w, h)
        self.component_surface = pygame.Surface(self.size, flags=pygame.SRCALPHA)
        self.components = [Mouse()]

        self.backdrop = pygame.Surface(self.size)
        tile = asset('sprites').subsurface(tuple(conf.values()))
        for j in range(int(h / block + 1)):
            for i in range(int(w / block + 1)):
                self.backdrop.blit(tile, (i * block, j * block))

        self.backdrop.set_alpha(60)

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

    def render(self, surface):
        surface.blit(self.backdrop, (0,0))

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
