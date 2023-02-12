import time

from src.app.state_machine.actions.action__ import BaseAction


class ActionSay(BaseAction):

    def __init__(self, app, parent_state, text_to_say, emote=None):
        super().__init__(app, parent_state)
        self.text_to_say = text_to_say
        self.emote = emote

    def start(self):
        super().start()

        if self.emote is not None:
            self.app.eq_chat.emote(self.emote)

        self.app.eq_chat.say(self.text_to_say)

        self.on_complete()
