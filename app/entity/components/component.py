import pygame

from abc import ABCMeta, abstractmethod
from app.entity import RenderableEntity


class Component(RenderableEntity):

    def __init__(self, type):
        super().__init__()
        self.type = type

    def update(self, delta):
        mouse = pygame.mouse.get_pos()

        self.on_move(mouse)
        if self.intersects(mouse):
            print('intersecting')
            self.on_hover()

            if pygame.mouse.get_pressed()[0]:
                self.on_press()

    @abstractmethod
    def on_mount(self):
        pass

    @abstractmethod
    def on_hover(self):
        pass

    @abstractmethod
    def on_press(self):
        pass

    @abstractmethod
    def on_move(self, pos):
        pass
