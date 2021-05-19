import pygame
import random

from . import State
from app.types import PieceType
from app.entity import Piece
from app.types import EntityType
from app.entity.components import Button


class MenuState(State):

    def start(self):
        w = config('display.width')
        h = config('display.height')

        bw = config('sprites.box.width')
        bh = config('sprites.box.height')

        self.pos = ((w - bw) / 2, (h - bh) / 2)

        bw = config('sprites.button.width')
        bh = config('sprites.button.height')

        btn_start = Button()
        btn_start.set_pos((w - bw) / 2, (h - bh) / 2)
        btn_start.handle(lambda : emit('play'))
        self.add_component(btn_start)

        self.pieces = []
        self.buffer = []
        self.available = [i for i in PieceType]
        self.spawn_time = 0
        self.spawn_delay = 2
        self.spawner = self.spawn()

        super().start()

    def update(self, delta):
        super().update(delta)

        current_time = pygame.time.get_ticks()
        time_since_spawn = (current_time - self.spawn_time) / 1000.0
        if time_since_spawn >= self.spawn_delay:
            self.spawn_time = current_time
            piece = Piece(next(self.spawner))
            piece.set_pos(random.randint(0, config('display.width')), -40)
            self.pieces.append(piece)

        for piece in self.pieces:
            piece.inc_y(126 * delta)
            piece.update(delta)

    def render(self, surface):
        super().render(surface)

        for piece in self.pieces:
            piece.render(surface)

        draw(surface, 'sprites.box', self.pos)

    def on_key(self, key):
        pass

    def restart(self):
        pass

    def spawn(self):
        while True:
            index = random.randint(0, len(self.available)-1)
            yield self.available[index]
