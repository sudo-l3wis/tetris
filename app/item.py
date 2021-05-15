class GridItem:

    def __init__(self, entity):
        self.entity = entity
        self.grid_x = 0
        self.grid_y = 0
        self.grid_width = 0
        self.grid_height = 0
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

    def set_grid_width(self, grid_width):
        self.grid_width = grid_width

    def get_grid_width(self):
        return self.grid_width

    def set_grid_height(self, grid_height):
        self.grid_height = grid_height

    def get_grid_height(self):
        return self.grid_height

    def get_width(self):
        return self.entity.get_width()

    def get_height(self):
        return self.entity.get_height()

    def render(self, surface):
        x = self.grid_x * self.block
        y = self.grid_y * self.block

        self.entity.set_pos(x, y)
        self.entity.render(surface)
