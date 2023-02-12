from src.app.config import Config
from src.app.eq_logs.eq_log_file import EQLogFile
from src.app.thread.eq_log_events import EQLogEvents
from src.app.thread.thread_with_events import ThreadWithEvents


class EQLogThread(ThreadWithEvents):
    def __init__(self, config: Config):
        super().__init__(config, EQLogEvents())

    def create_thread(self, *args):
        logfile = EQLogFile(*args)
        logfile.open()
        logfile.run()

    def push_log_event(self, new_event):
        self.events.push_log_event(new_event)

    def try_get_next_log_event(self):
        return self.events.try_get_next_log_event()
