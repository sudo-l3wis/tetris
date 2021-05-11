from . import MetaSingleton
from app.state import MenuState


class StateManager(metaclass=MetaSingleton):

    def __init__(self, *states):
        self.states = states
        self.state = MenuState()

    def start(self):
        self.state.start()

    def change(self, state):
        self.state = self.states[state.value()]
        self.state.start()

    def update(self, delta):
        self.state.update(delta)

    def render(self, surface):
        self.state.render(surface)
        self.state.render_ui(surface)
