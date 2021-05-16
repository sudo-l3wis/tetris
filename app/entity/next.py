from . import RenderableEntity


class NextPiece(RenderableEntity):

    def __init__(self):
        super().__init__()
        conf = config('sprites.box')
        self.set_surface(asset('sprites').subsurface(tuple(conf.values())))
        self.set_width(conf['width'])
        self.set_height(conf['height'])
        self.piece = None

    def render(self, surface):
        super().render(surface)
        if self.piece is not None:
            x, y = self.get_origin()
            width = self.piece.get_width()
            height = self.piece.get_height()
            self.piece.render_at(surface, x - width / 2, y - height / 2)

    def set(self, piece):
        self.piece = piece
