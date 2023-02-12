from src.app.eq_logs.eq_log_event import EQLogEvent
from src.app.state_machine.actions.action_say import ActionSay
from src.app.state_machine.actions.action_target import ActionTarget


class EQLogEventHail(EQLogEvent):

    def get_triggers(self):
        return [
            '^(\w+) say, \'Hail, (\w+)\'',
            '^(\w+) says, \'Hail, (\w+)\'',
        ]

    def run(self, app):
        hailed_name = self.match.group(2)
        if hailed_name == app.config.get("eq_char_name"):
            their_name = self.match.group(1)
            self.respond(app, their_name)

    def respond(self, app, their_name):

        response = f"The God of Fear has laid his eyes upon you, {their_name}, and he sees potential... Cazic Thule desires those who will embrace darkness, those who are willing to bleed and to die for him and carry on his [Legacy]."

        action = ActionTarget(app, None, their_name)
        action.start()
        action = ActionSay(app, None, response, "/eye")
        action.start()


