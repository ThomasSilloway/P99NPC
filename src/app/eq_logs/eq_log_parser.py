import re
from src.app.eq_logs.eq_log_event_hail import EQLogEventHail


class EQLogParser:

    def __init__(self):
        self.events = [
            EQLogEventHail,
        ]

    # regex match?
    def try_create_event_for_line_raw(self, line):
        # cut off the leading date-time stamp info
        trunc_line = line[27:]

        return self.try_create_event_for_line(trunc_line)

    # regex match?
    def try_create_event_for_line(self, trunc_line):
        # walk thru the target list and trigger list and see if we have any match
        for new_event in self.events:
            triggers = new_event.get_triggers()
            for trigger in triggers:
                # return value m is either None of an object with information about the RE search
                match = re.match(trigger, trunc_line)
                if match:
                    return new_event(trunc_line, match)

        # only executes if loops did not return already
        return None

    def parse(self, line):
        new_event = self.try_create_event_for_line_raw(line)

        if line:
            return new_event
