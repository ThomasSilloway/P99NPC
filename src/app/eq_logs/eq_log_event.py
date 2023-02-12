class EQLogEvent:
    triggers = [
        '^(\w+) say, \'Hail, (\w+)\'',
        '^(\w+) says, \'Hail, (\w+)\'',
    ]

    def __init__(self, log_line, match):
        self.log_line = log_line
        self.match = match

    def run(self, app):
        pass

    @classmethod
    def get_triggers(cls):
        pass
