import pygame
import random

from . import RenderableEntity
from . import NextPiece

from app.types import PieceType
from app.entity import Piece

class Board(RenderableEntity):

    def __init__(self, grid):
        super().__init__()

        self.grid = grid
        self.buffer = 0
        self.move_time = 0
        self.move_delay = 1

        self.spawner = self.spawn()
        self.available = [i for i in PieceType]

        piece = Piece(next(self.spawner))
        self.next_piece = NextPiece()
        self.next_piece.set(piece)
        self.next_piece.set_x(config('display.width') - config('sprites.box.width') - 15)
        self.next_piece.set_y(15)
        self.grid.add(piece)
        self.buffer = [Piece(next(self.spawner)) for i in range(3)]

        conf = config('sprites.board')
        self.set_surface(asset('sprites').subsurface(tuple(conf.values())))
        self.set_width(conf['width'])
        self.set_height(conf['height'])

    def update(self, delta):
        super().update(delta)

        if self.grid.is_pending():
            self.grid.add(self.buffer.pop())
            piece = Piece(next(self.spawner))
            self.buffer.append(piece)
            self.next_piece.set(piece)

        current_time = pygame.time.get_ticks()
        time_since_move = (current_time - self.move_time) / 1000.0
        if time_since_move >= self.move_delay:
            self.move_time = current_time
            self.grid.tick()


    def render(self, surface):
        super().render(surface)
        self.grid.render(surface)
        self.next_piece.render(surface)

    def on_key(self, key):
        if key == pygame.K_LEFT:
            emit('controls.left', self.grid)
        elif key == pygame.K_RIGHT:
            emit('controls.right', self.grid)
        elif key == pygame.K_DOWN:
            emit('controls.down', self.grid)

    def spawn(self):
        while True:
            index = random.randint(0, len(self.available)-1)
            yield self.available[index]
