from src.app.eq_logs.eq_log_event_quest_keyword import EQLogEventQuestKeyword
from src.app.state_machine.actions.action__ import BaseAction
from src.app.state_machine.states.state_validate_ik_requirements import StateValidateIkRequirements


class ActionListenForQuests(BaseAction):

    def __init__(self, app, parent_state):
        super().__init__(app, parent_state)
        self.player_name = None

    def start(self):
        super().start()

        self.app.event_manager.register_event_handler(EQLogEventQuestKeyword, self.on_quest_keyword)

    def on_quest_keyword(self, event):
        if event.keyword == "FOR IK!":
            self.player_name = event.get_player_name()
            # Only for testing, ideally "You" should never be the player name for quests
            if self.player_name == "You":
                self.player_name = self.app.config.get("eq_char_name")
            self.app.event_manager.unregister_event_handler(EQLogEventQuestKeyword, self.on_quest_keyword)
            self.app.state_machine.queue_state(StateValidateIkRequirements)
            self.app.state_machine.start_queued_state(self.on_validate_ik_requirements_started)

    def on_validate_ik_requirements_started(self, state):
        state.set_data(self.player_name)
