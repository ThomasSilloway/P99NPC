import logging

from src.app.eq_logs.eq_log_event_who import EQLogEventWho
from src.app.state_machine.actions.action__ import BaseAction
from src.app.state_machine.actions.action_say import ActionSay


class ActionCheckIkReqWho(BaseAction):

    def start(self):
        super().start()

        self.app.event_manager.register_event_handler(EQLogEventWho, self.on_who)

        self.app.eq_chat.send_command(f"/who {self.parent_state.player_name}")
        # TODO Should probably do some timeout if something goes wrong?

    def on_who(self, event):
        if event.get_character_name() == self.parent_state.player_name:
            self.app.event_manager.unregister_event_handler(EQLogEventWho, self.on_who)
            race = event.get_race()
            if race != "Iksar":
                self.failed_check("You are not an Iksar... be gone{!}")
                return

            level = event.get_level()
            if level > 6:
                self.failed_check("You are too high level... be gone{!}")
                return

            self.on_complete()

    def failed_check(self, message):
        action = ActionSay(self.app, self.parent_state, message)
        action.start()
        self.parent_state.failed_check()
