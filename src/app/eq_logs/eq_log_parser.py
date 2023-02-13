import json
import logging
import re
from src.app.eq_logs.eq_log_event_hail import EQLogEventHail
from src.app.eq_logs.eq_log_event_quest_keyword import EQLogEventQuestKeyword
from src.app.eq_logs.eq_log_event_who import EQLogEventWho


class EQLogParser:

    def __init__(self):
        self.events = [
            EQLogEventHail(),
            EQLogEventWho(),
        ]

        self.populate_quest_events()

    def populate_quest_events(self):
        # Open the JSON file
        with open(f".\\content\\quests.json", 'r') as f:
            # Load the array from the JSON file
            quest_list = json.load(f)

        for quest in quest_list:
            new_event = EQLogEventQuestKeyword(quest["keyword"], quest["response"], quest["emote"])
            self.events.append(new_event)

    # Script:

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
                match = re.match(trigger, trunc_line)
                if match:
                    return new_event.set_parsed_data(trunc_line, match)

        # only executes if loops did not return already
        return None

    def parse(self, line):
        new_event = self.try_create_event_for_line_raw(line)

        if line:
            return new_event
