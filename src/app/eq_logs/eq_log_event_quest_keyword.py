from src.app.eq_logs.eq_log_event import EQLogEvent
from src.app.state_machine.actions.action_say import ActionSay
from src.app.state_machine.actions.action_target import ActionTarget


class EQLogEventQuestKeyword(EQLogEvent):

    def __init__(self, keyword, response, emote):
        super().__init__()
        self.keyword = keyword
        self.response = response
        self.emote = emote

    def get_triggers(self):
        return [
            f'^(\w+) say, \'.*{self.keyword}.*\'',
            f'^(\w+) says, \'.*{self.keyword}.*\'',
        ]

    def get_player_name(self):
        return self.match.group(1)

    def should_trigger(self, app):
        if self.get_player_name() == "You":
            return False
        return True
