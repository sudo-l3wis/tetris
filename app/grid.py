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
        self.item.set_grid_x(int(self.cols / 2 - int(piece.get_width() / self.block / 2)))
        self.item.set_grid_width(int(self.item.get_width() / self.block))
        self.item.set_grid_height(int(self.item.get_height() / self.block))

    def move_left(self):
        if not self.item:
            return

        if self.item.get_grid_x() > 0:
            self.item.inc_grid_x(-1)

    def move_right(self):
        if not self.item:
            return

        if self.item.get_grid_x() + self.item.get_grid_width() < self.cols:
            self.item.inc_grid_x(1)

    def move_down(self):
        if not self.item:
            return

        while self.tick():
            continue

    def tick(self):
        if not self.item:
            return False

        x, y, w, h = self.item_pos()

        if y + h >= self.rows:
            self.assign_cells()
            return False

        # Check for collisions.
        for i in range(w):
            if self.cells[y + h - 1][w + i] > -1:
                self.assign_cells()
                return False

        self.item.inc_grid_y(1)

        return True

    def assign_cells(self):
        x, y, w, h = self.item_pos()
        for j in range(y, y + h):
            for i in range(x, x + w):
                self.cells[j][i] = 1

        self.items.append(self.item)
        self.item = None

    def item_pos(self):
        x = self.item.get_grid_x()
        y = self.item.get_grid_y()
        w = self.item.get_grid_width()
        h = self.item.get_grid_height()

        return x, y, w, h

    def is_pending(self):
        return self.item is None
