from . import MovableEntity


class Piece(MovableEntity):

    def __init__(self, type):
        super().__init__()
        self.conf = config(type.value)
        bounds = (self.conf['x'], self.conf['y'], self.conf['width'], self.conf['height'])
        self.set_surface(asset('sprites').subsurface(bounds))
        self.cols = 0
        self.rows = 0
        self.state = -1
        self.states = self.conf['cells']
        self.cells = None
        self.next_state()

    def render_at(self, surface, x, y):
        block = config('display.grid.block')
        for j in range(self.rows):
            for i in range(self.cols):
                if self.cells[j][i] == 1:
                    surface.blit(self.get_surface(), (x + i * block, y + j * block))

    def render(self, surface):
        self.render_at(surface, *self.get_pos())

    def next_state(self):
        self.state = (self.state + 1) % len(self.states)
        cells = self.conf['cells'][self.state]
        self.cells = [[int(i) for i in j.split(',')] for j in cells]

        block = config('display.grid.block')

        self.cols = len(self.cells[0])
        self.rows = len(self.cells)
        self.set_width(self.cols * block)
        self.set_height(self.rows * block)
