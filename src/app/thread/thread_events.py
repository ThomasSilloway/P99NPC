import queue


class ThreadEvents:

    def check_event(self, event_to_check):
        if event_to_check.is_set():
            event_to_check.clear()
            return True

        return False

    def trigger_event(self, event_to_set):
        event_to_set.set()

    def try_get_next_item_in_queue(self, queue_to_check):
        try:
            return queue_to_check.get(block=False)
        except queue.Empty:
            return None
