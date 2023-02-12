import queue

from src.app.thread.thread_events import ThreadEvents


class EQLogEvents(ThreadEvents):

    def __init__(self):
        self.log_event_queue = queue.Queue()

    def push_log_event(self, new_event):
        self.log_event_queue.put(new_event)

    def try_get_next_log_event(self):
        return self.try_get_next_item_in_queue(self.log_event_queue)
