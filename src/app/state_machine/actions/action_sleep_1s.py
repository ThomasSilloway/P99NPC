import time

from src.app.state_machine.actions.action__ import BaseAction


class ActionSleep1s(BaseAction):

    def start(self):
        super().start()

        time.sleep(1)

        self.on_complete()
