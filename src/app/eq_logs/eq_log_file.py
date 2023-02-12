import logging
import os
import re
import time

from src.app.eq_logs.eq_log_event import EQLogEvent
from src.app.eq_logs.eq_log_parser import EQLogParser
from src.app.thread.eq_log_events import EQLogEvents


class EQLogFile:
    """
    class to encapsulate log file operations
    """

    def __init__(self, config, events: EQLogEvents):

        self.config = config
        self.events = events

        # instance data
        self.base_directory = config.get("eq_base_directory")
        self.char_name = config.get("eq_char_name")
        self.server_name = config.get("eq_server_name")
        self.filename = ''
        self.file = None

        # build the filename
        self.build_filename()

        self.event_parser = EQLogParser()

    def build_filename(self):
        self.filename = f"{self.base_directory}\\Logs\\eqlog_{self.char_name}_{self.server_name}.txt"

    # open the file
    # seek file position to end of file if passed parameter 'seek_end' is true
    def open(self, seek_end=True):
        self.file = open(self.filename)
        if seek_end:
            self.file.seek(0, os.SEEK_END)

    # close the file
    def close(self):
        self.file.close()

    def run(self):
        logging.info('EQ Log File Parsing Started')
        logging.info('Make sure to turn on logging in EQ with /log command!')

        # process the log file lines here
        while True:
            # read a line
            line = self.file.readline()
            if line:
                logging.info(line)
                new_event = self.event_parser.parse(line)
                if new_event:
                    self.events.push_log_event(new_event)

            time.sleep(0.1)

