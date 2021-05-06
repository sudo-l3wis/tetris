import pygame

from app.types import Cardinal

from . import StateBasedEntity


class MovableEntity(StateBasedEntity):
    def __init__(self):
        super().__init__()
        self.__velocity = 0
        self.__direction = None
        self.rotation = 0

    def get_direction(self):
        return self.__direction

    def set_direction(self, direction):
        self.__direction = direction

    def get_velocity(self):
        return self.__velocity

    def set_velocity(self, velocity):
        self.__velocity = velocity

    def rotate(self, rotation):
        self.rotation = rotation

    def update(self, delta):
        super().update(delta)

        if self.__direction == Cardinal.NORTH:
            self.inc_y(-self.__velocity * delta)
        elif self.__direction == Cardinal.EAST:
            self.inc_x(self.__velocity * delta)
        elif self.__direction == Cardinal.SOUTH:
            self.inc_y(self.__velocity * delta)
        elif self.__direction == Cardinal.WEST:
            self.inc_x(-self.__velocity * delta)

    def get_surface(self):
        surface = super().get_surface()
        if self.rotation:
            return pygame.transform.rotate(surface, self.rotation)
        return surface
