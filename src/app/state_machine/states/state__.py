import logging


class BaseState:

    def __init__(self, app):
        self.app = app
        self.actions = self.create_action_list()
        self.current_action = None
        self.transition_to_chatting_queued = False

    def start(self):
        self.current_action = self.start_next_action()

    def resume(self):
        # I think this can be the same as start since it'll take over where it left off, not sure though
        self.start()

    def create_action_list(self):
        return []

    def update(self):
        if self.current_action is None:
            return

        self.current_action.update()

        if self.current_action is None:
            return

        if self.current_action.is_complete:
            if self.app.state_machine.has_queued_state():
                self.app.state_machine.start_queued_state()
            else:
                self.current_action = self.start_next_action()

    def on_complete(self):
        pass

    def start_next_action(self):

        if len(self.actions) == 0:
            # print(f"{self} all actions complete")
            self.on_complete()
            return None

        next_action_data = self.actions.pop(0)
        # Next action can either be a class to start, or an already created action that needs to be resumed
        type_a = type(next_action_data)
        if type_a is type:
            next_action = next_action_data(self.app, self)
            next_action.start()
        else:
            next_action = next_action_data
            next_action.resume()

        return next_action

    def return_to_previous_state(self, callback):
        return False
