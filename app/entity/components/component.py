import pygame

from abc import ABCMeta, abstractmethod
from app.entity import RenderableEntity


class Component(RenderableEntity):

    def update(self, delta):
        super().update(delta)

        mouse = pygame.mouse.get_pos()

        self.on_move(mouse)
        if self.intersects(mouse):
            self.on_hover()

            if pygame.mouse.get_pressed()[0]:
                self.on_press()

        else:
            self.on_leave()

    @abstractmethod
    def on_mount(self):
        pass

    @abstractmethod
    def on_hover(self):
        pass

    @abstractmethod
    def on_leave(self):
        pass

    @abstractmethod
    def on_press(self):
        pass

    @abstractmethod
    def on_move(self, pos):
        pass
