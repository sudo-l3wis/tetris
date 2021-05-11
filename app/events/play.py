from app.types import State
from app.framework.singleton import StateManager
from app.framework.decorator import inject


class PlayEvent:

    @inject('state.manager')
    def handle(event, manager):
        manager.change(State.RUNNING)
