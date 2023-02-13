from src.app.eq_logs.eq_log_event import EQLogEvent
from src.app.state_machine.actions.action_say import ActionSay
from src.app.state_machine.actions.action_target import ActionTarget


class EQLogEventWho(EQLogEvent):

    # [1 Warrior] Tomtomtom (Halfling)
    def get_triggers(self):
        return [
            '^\[(\d+) (\w+)\] (\w+) \((\w+)\)',
        ]

    def should_trigger(self):
        return True

    def get_level(self):
        return int(self.match.group(1))

    def get_class_name(self):
        return self.match.group(2)

    def get_character_name(self):
        return self.match.group(3)

    def get_race(self):
        return self.match.group(4)


