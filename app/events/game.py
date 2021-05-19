from app.types import State
from app.framework.singleton import StateManager
from app.framework.decorator import inject


class GameOver:

    @inject('singleton.state')
    def handle(self, _next, manager):
        manager.restart()
        return next(_next)
