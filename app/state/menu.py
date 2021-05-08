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
        draw(surface, 'sprites.board', (0, 0))
        draw(surface, 'sprites.pieces.I', (0, 0))
        draw(surface, 'sprites.box')
        draw(surface, 'sprites.extended_box')
        #draw(surface, 'sprites.button')
        #draw(surface, 'sprites.icon_play')
        #draw(surface, 'sprites.pieces.I', (20, 20))
