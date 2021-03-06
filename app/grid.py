import pygame

from . import GridItem


class Grid:

    def __init__(self, offset_x, offset_y):
        self.offset_x = offset_x
        self.offset_y = offset_y
        self.cells = [[None for i in range(10)] for j in range(13)]
        self.cols = config('display.grid.cols')
        self.rows = config('display.grid.rows')
        self.block = config('display.grid.block')
        self.item = None

        width = self.block * self.cols
        height = self.block * self.rows

        self.surface = pygame.Surface((width, height), flags=pygame.SRCALPHA)

    def reset(self):
        self.cells = [[None for i in range(10)] for j in range(13)]
        self.item = None

    def update(self, delta):
        # Check for complete line.
        lines = 0
        for j in range(len(self.cells)):
            if None not in self.cells[j]:
                self.cells.pop(j)
                self.cells.insert(0, [None for i in range(self.cols)])
                lines += 1

        if lines > 0:
            emit('score.line', lines)

    def render(self, surface):
        self.surface.fill((0, 0, 0, 0))

        if self.item is not None:
            self.item.render(self.surface)

        for j in range(len(self.cells)):
            for i in range(len(self.cells[j])):
                if self.cells[j][i] is not None:
                    _surface = self.cells[j][i].entity.get_surface()
                    pos = (i * self.block, j * self.block)
                    self.surface.blit(_surface, pos)

        surface.blit(self.surface, (self.offset_x, self.offset_y))

    def add(self, piece):
        self.item = GridItem(piece)
        self.item.set_grid_x(int((self.cols - piece.cols) / 2))

    def tick(self):
        if not self.item:
            return False

        x, y, w, h = self.item.pos()

        # Check for game over.
        for j in range(h):
            for i in range(w):
                if self.item.is_fill(i, j):
                    if self.cells[y+j][x+i] is not None:
                        emit('game.over')
                        return False

        # Check for bottom.
        if y + h >= self.rows:
            self.assign_cells()
            return False

        # Check for vertical collisions.
        for j in range(h):
            for i in range(w):
                if self.item.is_fill(i, j):
                    if self.cells[y+j+1][x+i] is not None:
                        self.assign_cells()
                        return False

        self.item.inc_grid_y(1)

        return True

    def assign_cells(self):
        x, y, w, h = self.item.pos()

        # Assign cells.
        for j in range(h):
            for i in range(w):
                if self.item.is_fill(i, j):
                    self.cells[y+j][x+i] = self.item

        self.item = None

    def rotate(self):
        self.item.rotate()

    def current(self):
        return self.item

    def is_pending(self):
        return self.item is None
