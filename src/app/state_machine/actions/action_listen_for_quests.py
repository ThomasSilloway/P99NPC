from src.app.eq_logs.eq_log_event_hail import EQLogEventHail
from src.app.eq_logs.eq_log_event_quest_keyword import EQLogEventQuestKeyword
from src.app.state_machine.actions.action__ import BaseAction
from src.app.state_machine.actions.action_say import ActionSay
from src.app.state_machine.actions.action_target import ActionTarget
from src.app.state_machine.states.state_validate_ik_requirements import StateValidateIkRequirements


class ActionListenForQuests(BaseAction):

    def __init__(self, app, parent_state):
        super().__init__(app, parent_state)
        self.player_name = None

    def start(self):
        super().start()

        self.app.event_manager.register_event_handler(EQLogEventQuestKeyword, self.on_quest_keyword)
        self.app.event_manager.register_event_handler(EQLogEventHail, self.on_hail)

    def on_hail(self, event):
        their_name = event.get_their_name()
        response = f"The God of Fear has laid his eyes upon you, {their_name}, and he sees potential... Cazic Thule desires those who will embrace darkness, those who are willing to bleed and to die for him and carry on his [Legacy]."
        emote = "/eye"
        self.respond_to_event(event, their_name, response, emote)

    def on_quest_keyword(self, event):
        if event.keyword == "FOR IK!":
            self.player_name = event.get_player_name()
            # Only for testing, ideally "You" should never be the player name for quests
            if self.player_name == "You":
                self.player_name = self.app.config.get("eq_char_name")
            self.app.event_manager.unregister_event_handler(EQLogEventQuestKeyword, self.on_quest_keyword)
            self.app.event_manager.unregister_event_handler(EQLogEventHail, self.on_hail)
            self.app.state_machine.queue_state(StateValidateIkRequirements)
            self.app.state_machine.start_queued_state(self.on_validate_ik_requirements_started)
        else:
            # Handle normal quests
            their_name = event.get_player_name()
            response = event.response.replace("<name>", their_name)

            self.respond_to_event(event, their_name, response, event.emote)

    def respond_to_event(self, event, their_name, response, emote):
        action = ActionTarget(self.app, None, their_name)
        action.start()
        action = ActionSay(self.app, None, response, emote)
        action.start()

    def on_validate_ik_requirements_started(self, state):
        state.set_data(self.player_name)
