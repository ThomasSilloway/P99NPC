import logging
import time
from ahk import AHK

from src.app.eq_commands.eq_chat import EQChat
from src.app.eq_logs.eq_log_parser import EQLogParser
from src.app.state_machine.actions.action_say import ActionSay
from src.app.thread.eq_log_thread import EQLogThread


class App:
    PROCESS_TIME_INTERVAL = 0.5

    def __init__(self, config):
        self.config = config

        window_name = self.config.get("eq_window_name")
        ahk = AHK()
        win = ahk.find_window(title=window_name.encode())
        win.activate()

        self.eq_chat = EQChat(ahk, win)

        self.eq_log_thread = EQLogThread(self.config)

    def run(self):

        while True:
            time.sleep(self.PROCESS_TIME_INTERVAL)

            new_event = self.eq_log_thread.try_get_next_log_event()
            if new_event is not None:
                new_event.run(self)

        # Run who command
        # while True:
        #     if win.active:
        #         # Run who command to make sure text input is cleared out
        #         ahk.send("/{enter}")
        #     if win.active:
        #         ahk.send("/who all \"Legacy of Ik\"{enter}")
        #         time.sleep(3)
