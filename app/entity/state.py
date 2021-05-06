from . import AnimatedEntity


class StateBasedEntity(AnimatedEntity):
    def __init__(self):
        super().__init__()
        self.__state = ''
        self.__states = {}

    def get_state(self):
        return self.__state

    def set_state(self, state):
        self.__state = state
        self.set_frame(0)
        self.set_frames(self.__states[state])
        self.animation_complete = False

    def get_states(self):
        return self.__states

    def set_states(self, states):
        self.__states = states
