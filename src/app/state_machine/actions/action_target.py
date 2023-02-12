import time

from src.app.state_machine.actions.action__ import BaseAction


class ActionTarget(BaseAction):

    def __init__(self, app, parent_state, player_to_target):
        super().__init__(app, parent_state)
        self.player_to_target = player_to_target

    def start(self):
        super().start()

        self.app.eq_chat.target(self.player_to_target)

        self.on_complete()
