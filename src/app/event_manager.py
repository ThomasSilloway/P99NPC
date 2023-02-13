class EventManager:
    def __init__(self):
        self.event_handlers = {}

    def register_event_handler(self, event_class, callback):
        if event_class not in self.event_handlers:
            self.event_handlers[event_class] = []
        self.event_handlers[event_class].append(callback)

    def unregister_event_handler(self, event_class, callback):
        if event_class in self.event_handlers:
            self.event_handlers[event_class].remove(callback)

    def trigger(self, event):
        event_class = type(event)
        if event_class in self.event_handlers:
            for callback in self.event_handlers[event_class]:
                callback(event)
