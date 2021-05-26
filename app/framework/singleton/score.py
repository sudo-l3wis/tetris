from . singleton import MetaSingleton


class Score(metaclass=MetaSingleton):

    def __init__(self):
        super().__init__()
        self.score = 0

    def set_score(self, score):
        self.score = score

    def inc_score(self, i):
        self.score += i

    def get_score(self):
        return self.score
