import logging


class StateMachine:

    def __init__(self, app):
        self.app = app
        self.state = None
        # A representation of states that were already started
        # and they were interrupted, so we can go back to them
        self.previous_state_stack = []
        self.queued_state = None

    def start_state(self, new_state_class):
        self.create_state(new_state_class)
        self.state.start()
        logging.info(f"Entered state: {self.state.__class__.__name__}")

    def create_state(self, new_state_class):
        self.state = new_state_class(self.app)

    def update(self):
        self.state.update()

    def queue_state(self, new_state_class):
        if self.queued_state is not None:
            logging.warning(f"Unable to queue state: {new_state_class.__name__} because {self.queued_state.__name__} is already in the queue")
        else:
            self.queued_state = new_state_class
            logging.info(f"Queued State: {new_state_class.__name__}")

    def has_queued_state(self):
        return self.queued_state is not None

    def start_queued_state(self):
        self.previous_state_stack.insert(0, self.state)
        # logging.info(f"Start queued state: {self.queued_state.__name__}")
        # self.debug_state_stack()
        self.start_state(self.queued_state)
        self.queued_state = None

    def try_return_to_previous_state(self):
        # Run any action that needs to happen before returning to the previous state, like playing a transition
        if not self.state.return_to_previous_state(self.return_to_previous_state):
            self.return_to_previous_state()

    def return_to_previous_state(self):
        self.state = self.previous_state_stack.pop(0)
        # print(f"Resuming previous state: {self.state.__class__.__name__}")
        # self.debug_state_stack()
        self.state.resume()

    def debug_state_stack(self):
        logging.info(f"State stack has {len(self.previous_state_stack)} entries")

    def has_pending_previous_states(self):
        return len(self.previous_state_stack) > 0
