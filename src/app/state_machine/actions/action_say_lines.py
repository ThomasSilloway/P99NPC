import time

from src.app.state_machine.actions.action__ import BaseAction


class ActionSayLines(BaseAction):

    def __init__(self, app, parent_state, text_to_say):
        super().__init__(app, parent_state)
        self.text_to_say = text_to_say

    def start(self):
        super().start()

        lines_to_say = self.text_to_say.split(". ")

        for line in lines_to_say:
            self.app.eq_chat.say(line + ".")

        self.on_complete()
