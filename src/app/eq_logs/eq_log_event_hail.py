from src.app.eq_logs.eq_log_event import EQLogEvent
from src.app.state_machine.actions.action_say import ActionSay


class EQLogEventHail(EQLogEvent):

    @classmethod
    def get_triggers(cls):
        return [
            '^(\w+) say, \'Hail, (\w+)\'',
            '^(\w+) says, \'Hail, (\w+)\'',
        ]

    def run(self, app):
        hailed_name = self.match.group(2)
        if hailed_name == app.config.get("eq_char_name"):
            their_name = self.match.group(1)
            action = ActionSay(app, None, f"I don't have time for that right now, {their_name}.")
            action.start()
