import pygame
import random

from . import RenderableEntity
from app.types import PieceType
from app.entity import Piece


class Board(RenderableEntity):

    def __init__(self, grid):
        self.grid = grid
        self.buffer = 0
        self.spawner = self.spawn()
        self.available = [i for i in PieceType]
        self.piece = Piece(next(self.spawner))
        self.grid.add(self.piece)
        self.buffer = [Piece(next(self.spawner)) for i in range(3)]
        self.move_time = 0
        self.move_delay = 1

        conf = config('sprites.board')
        self.set_surface(asset('sprites').subsurface(tuple(conf.values())))
        self.set_width(conf['width'])
        self.set_height(conf['height'])

    def update(self, delta):
        super().update(delta)

        if self.piece is None:
            self.piece = self.buffer.pop()
            self.buffer.append(Piece(next(self.spawner)))

        current_time = pygame.time.get_ticks()
        time_since_move = (current_time - self.move_time) / 1000.0
        if time_since_move >= self.move_delay:
            self.move_time = current_time
            self.grid.tick()

    def render(self, surface):
        super().render(surface)
        self.grid.render(surface)

    def spawn(self):
        while True:
            index = random.randint(0, len(self.available)-1)
            yield self.available[index]
