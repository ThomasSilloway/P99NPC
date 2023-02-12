import threading

from src.app.config import Config


class ThreadWithEvents:

    def __init__(self, config: Config, events):
        self.config = config
        self.events = events
        self.thread = threading.Thread(target=self.create_thread, args=self.get_args())
        self.thread.start()

    def get_args(self):
        return [self.config, self.events]

    def create_thread(self, *args):
        pass
