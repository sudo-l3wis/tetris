import pygame

from . import GridItem


class Grid:

    def __init__(self, offset_x, offset_y):
        self.offset_x = offset_x
        self.offset_y = offset_y
        self.cells = [[-1 for i in range(10)] for j in range(13)]
        self.cols = config('display.grid.cols')
        self.rows = config('display.grid.rows')
        self.block = config('display.grid.block')
        self.items = []
        self.item = None

        width = self.block * self.cols
        height = self.block * self.rows

        self.surface = pygame.Surface((width, height), flags=pygame.SRCALPHA)

    def render(self, surface):
        self.surface.fill((0, 0, 0, 0))

        if self.item is not None:
            self.item.render(self.surface)

        for item in self.items:
            item.render(self.surface)

        surface.blit(self.surface, (self.offset_x, self.offset_y))

    def add(self, piece):
        self.item = GridItem(piece)
        self.item.set_grid_x(int((self.cols - piece.cols) / 2))

    def tick(self):
        if not self.item:
            return False

        x, y, w, h = self.item.pos()

        # Check for bottom.
        if y + h >= self.rows:
            self.assign_cells()
            return False

        # Check for collisions.
        for i in range(w):
            if self.item.is_bottom_fill(i):
                if self.cells[y + h][x + i] > -1:
                    self.assign_cells()
                    return False

        self.item.inc_grid_y(1)

        return True

    def assign_cells(self):
        x, y, w, h = self.item.pos()
        for j in range(h):
            for i in range(w):
                if self.item.is_fill(i, j):
                    self.cells[y + j][x + i] = 1

        self.items.append(self.item)
        self.item = None

    def current(self):
        return self.item

    def is_pending(self):
        return self.item is None
