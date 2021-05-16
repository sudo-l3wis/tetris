from . import MovableEntity


class Piece(MovableEntity):

    def __init__(self, type):
        super().__init__()
        conf = config(type.value)
        bounds = (conf['x'], conf['y'], conf['width'], conf['height'])
        block = config('display.grid.block')
        self.set_surface(asset('sprites').subsurface(bounds))
        self.cols = conf['cols']
        self.rows = conf['rows']
        self.set_width(self.cols * block)
        self.set_height(self.rows * block)
        self.cells = [[int(i) for i in j.split(',')] for j in conf['cells']]

    def render_at(self, surface, x, y):
        block = config('display.grid.block')
        for j in range(self.rows):
            for i in range(self.cols):
                if self.cells[j][i] == 1:
                    surface.blit(self.get_surface(), (x + i * block, y + j * block))

    def render(self, surface):
        self.render_at(surface, *self.get_pos())
