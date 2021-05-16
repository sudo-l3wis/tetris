class GridItem:

    def __init__(self, entity):
        self.entity = entity
        self.grid_x = 0
        self.grid_y = 0
        self.block = config('display.grid.block')

    def set_grid_x(self, grid_x):
        self.grid_x = grid_x

    def get_grid_x(self):
        return self.grid_x

    def inc_grid_x(self, x):
        self.grid_x += x

    def set_grid_y(self):
        self.grid_y = grid_y

    def get_grid_y(self):
        return self.grid_y

    def inc_grid_y(self, y):
        self.grid_y += y

    def get_grid_width(self):
        return self.entity.cols

    def get_grid_height(self):
        return self.entity.rows

    def get_width(self):
        return self.entity.get_width()

    def get_height(self):
        return self.entity.get_height()

    def pos(self):
        x = self.get_grid_x()
        y = self.get_grid_y()
        w = self.get_grid_width()
        h = self.get_grid_height()

        return x, y, w, h

    def is_fill(self, x, y):
        return self.entity.cells[y][x] == 1

    def render(self, surface):
        x = self.grid_x * self.block
        y = self.grid_y * self.block

        self.entity.set_pos(x, y)
        self.entity.render(surface)
