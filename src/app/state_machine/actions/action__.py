import logging


class BaseAction:

    def __init__(self, app, parent_state):
        self.app = app
        self.is_complete = False
        self.parent_state = parent_state

    def start(self):
        logging.info("Start Action: " + str(self.__class__.__name__))
        pass

    def update(self):
        pass

    def on_complete(self):
        self.is_complete = True

    def resume(self):
        # Hopefully this is a good base behavior to have
        self.start()
