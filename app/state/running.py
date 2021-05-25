from . import State
from app.entity import Board
from app import Grid
from app.entity.components import Label


class RunningState(State):

    def start(self):
        inset = config('display.board.inset')
        offset = config('display.board.offset')

        self.board = Board(Grid(offset, offset))
        self.board.set_pos(inset, inset)

        w = config('display.width')
        lbl_score = Label("score;")
        lw = lbl_score.get_width()
        lbl_score.set_pos(w - lw - 20, 320)
        self.add_component(lbl_score)

        self.score = 0
        score = self.score
        lbl_value = Label(f'{score:04}')
        lw = lbl_value.get_width()
        lbl_value.set_pos(w - lw - 40, 400)
        self.add_component(lbl_value)

        super().start()

    def update(self, delta):
        super().update(delta)
        self.board.update(delta)

    def render(self, surface):
        super().render(surface)
        self.board.render(surface)

    def on_key(self, key):
        super().on_key(key)
        self.board.on_key(key)

    def restart(self):
        self.board.reset()
