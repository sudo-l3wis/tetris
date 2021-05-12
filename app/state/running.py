from . import State
from app.entity import Board


class RunningState(State):

    def start(self):
        super().start()

        self.board = Board()
        self.board.set_pos(10, 10)

    def update(self, delta):
        super().update(delta)
        self.board.update(delta)

    def render(self, surface):
        super().render(surface)
        self.board.render(surface)
