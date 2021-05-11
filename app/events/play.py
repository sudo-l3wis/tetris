from app.types import State
from app.framework.singleton import StateManager
from app.framework.decorator import inject


class PlayEvent:

    @inject('singleton.state')
    def handle(self, _next, manager):
        manager.change(State.RUNNING)
        return next(_next)
