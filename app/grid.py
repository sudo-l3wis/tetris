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
        if self.item is not None:
            self.item.render(self.surface)
        surface.blit(self.surface, (self.offset_x, self.offset_y))

    def add(self, piece):
        self.item = GridItem(piece)

        b = self.block
        w = piece.get_width()
        c = self.cols

        self.item.set_grid_x(int(c / 2 - int(w / b / 2)))
        self.item.set_grid_width(int(self.item.get_width() / self.block))
        self.item.set_grid_height(int(self.item.get_height() / self.block))

    def tick(self):
        if not self.item:
            return

        x = self.item.get_grid_x()
        y = self.item.get_grid_y()
        w = self.item.get_grid_width()
        h = self.item.get_grid_height()

        # Check for bottom & assign cells.
        if y + h == self.rows:
            for j in range(y, y + h):
                for i in range(x, x + w):
                    self.cells[j][i] = 1
            self.item = None
            return

        # Check for collisions.
        is_empty = True
        for i in range(w):
            if self.cells[y + h][w + i] == 1:
                is_empty = False
                break

        self.item.inc_grid_y(1)
