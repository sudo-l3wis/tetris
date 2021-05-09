from . import State
from app.types import EntityType


class MenuState(State):

    def __init__(self):
        pass

    def start(self):
        pass

    def update(self, delta):
        pass

    def render(self, surface):
        w = config('display.width')
        h = config('display.height')

        bw = config('sprites.box.width')
        bh = config('sprites.box.height')

        offsetX = w - bw - 15

        draw(surface, 'sprites.box', (offsetX, 9))
        draw(surface, 'sprites.extended_box', (offsetX, bh + 20))

        draw(surface, 'sprites.board', (10, 10))


        #draw(surface, 'sprites.button')
        #draw(surface, 'sprites.icon_play')
        #draw(surface, 'sprites.pieces.I', (0, 0))
        #draw(surface, 'sprites.pieces.J', (0, 0))
        #draw(surface, 'sprites.pieces.L', (0, 0))
        #draw(surface, 'sprites.pieces.O', (0, 0))
        #draw(surface, 'sprites.pieces.S', (0, 0))
        draw(surface, 'sprites.pieces.T', (0, 0))
        #draw(surface, 'sprites.pieces.Z', (0, 0))
