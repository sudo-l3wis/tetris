import pygame

from . import GridItem


class Grid:

    def __init__(self, offset_x, offset_y):
        self.offset_x = offset_x
        self.offset_y = offset_y
        self.cells = [[0 for i in range(10)] for j in range(13)]
        self.cols = config('display.grid.cols')
        self.rows = config('display.grid.rows')
        self.block = config('display.grid.block')
        self.item = None

        width = self.block * self.cols
        height = self.block * self.rows

        self.surface = pygame.Surface((width, height), flags=pygame.SRCALPHA)

    def render(self, surface):
        self.surface.fill((0, 0, 0, 0))
        self.item.render(self.surface)
        surface.blit(self.surface, (self.offset_x, self.offset_y))

    def add(self, piece):
        self.item = GridItem(piece)

        b = self.block
        w = piece.get_width()
        c = self.cols

        self.item.set_grid_x(c / 2 - int(w / b / 2))

    def tick(self):
        self.item.inc_grid_y(1)
