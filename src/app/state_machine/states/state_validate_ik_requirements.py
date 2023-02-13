import logging

from src.app.state_machine.actions.action_check_ik_req_who import ActionCheckIkReqWho
from src.app.state_machine.states.state__ import BaseState


class StateValidateIkRequirements(BaseState):

    def __init__(self, app):
        super().__init__(app)
        self.player_name = None

    def create_action_list(self):
        return [
            ActionCheckIkReqWho(self.app, self)
        ]

    def set_data(self, player_name):
        self.player_name = player_name

    def failed_check(self):
        self.app.state_machine.return_to_previous_state()
