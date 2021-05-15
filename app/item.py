class GridItem:

    def __init__(self, entity):
        self.entity = entity
        self.grid_x = 0
        self.grid_y = 0
        self.block = config('display.grid.block')

    def set_grid_x(self, grid_x):
        self.grid_x = grid_x

    def inc_grid_x(self, x):
        self.grid_x += x

    def set_grid_y(self):
        self.grid_y = grid_y

    def inc_grid_y(self, y):
        self.grid_y += y

    def render(self, surface):
        x = self.grid_x * self.block
        y = self.grid_y * self.block

        self.entity.set_pos(x, y)
        self.entity.render(surface)
