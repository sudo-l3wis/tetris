from app.types import State
from app.framework.singleton import StateManager
from app.framework.decorator import inject


class GameOver:

    @inject(['singleton.state', 'singleton.score'])
    def handle(self, _next, manager, score):
        manager.restart()
        score.set_score(0)
        return next(_next)
