from . import MovableEntity


class Piece(MovableEntity):

    def __init__(self, type):
        super().__init__()
        conf = config(type.value)
        self.set_surface(asset('sprites').subsurface(tuple(conf.values())))
        self.set_width(conf['width'])
        self.set_height(conf['height'])
