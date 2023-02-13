import time
from ahk import AHK

from src.app.eq_commands.eq_chat import EQChat
from src.app.event_manager import EventManager
from src.app.state_machine.state_machine import StateMachine
from src.app.state_machine.states.state_quest_giver import StateQuestGiver
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

        self.event_manager = EventManager()

        self.state_machine = StateMachine(self)
        self.state_machine.start_state(StateQuestGiver)

    def run(self):

        while True:
            time.sleep(self.PROCESS_TIME_INTERVAL)

            # TODO: I could see this working with each state registering events to watch for
            # Or states and actions subscribing to certain events and determining what to do

            new_event = self.eq_log_thread.try_get_next_log_event()
            if new_event and new_event.should_trigger():
                self.event_manager.trigger(new_event)

        # Run who command
        # while True:
        #     if win.active:
        #         # Run who command to make sure text input is cleared out
        #         ahk.send("/{enter}")
        #     if win.active:
        #         ahk.send("/who all \"Legacy of Ik\"{enter}")
        #         time.sleep(3)
