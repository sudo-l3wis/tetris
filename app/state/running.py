from . import State
from app.entity import Board
from app import Grid


class RunningState(State):

    def start(self):
        super().start()

        inset = config('display.board.inset')
        offset = config('display.board.offset')

        self.board = Board(Grid(offset, offset))
        self.board.set_pos(inset, inset)

    def update(self, delta):
        super().update(delta)
        self.board.update(delta)

    def render(self, surface):
        super().render(surface)
        self.board.render(surface)
