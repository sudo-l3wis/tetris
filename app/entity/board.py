from . import RenderableEntity
from app.types import PieceType
from app.entity import Piece


class Board(RenderableEntity):

    def __init__(self):
        conf = config('sprites.board')
        self.set_surface(asset('sprites').subsurface(tuple(conf.values())))
        self.set_width(conf['width'])
        self.set_height(conf['height'])

    def update(self, delta):
        super().update(delta)

    def render(self, surface):
        super().render(surface)
