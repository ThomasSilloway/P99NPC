from src.app.state_machine.actions.action_listen_for_quests import ActionListenForQuests
from src.app.state_machine.states.state__ import BaseState


class StateQuestGiver(BaseState):

    def __init__(self, app):
        super().__init__(app)

    def create_action_list(self):
        return [ActionListenForQuests(self.app, self)]
