import time
from ahk import AHK

from src.app.eq_commands.eq_chat import EQChat
from src.app.state_machine.actions.action_say import ActionSay


class App:

    def __init__(self, config):
        self.config = config

        window_name = self.config.get("eq_window_name")
        ahk = AHK()
        win = ahk.find_window(title=window_name.encode())
        win.activate()

        self.eq_chat = EQChat(ahk, win)

    def run(self):

        time.sleep(0.1)

        action = ActionSay(self, None, "I don't have time for that right now.")
        action.start()

        # Run who command
        # while True:
        #     if win.active:
        #         # Run who command to make sure text input is cleared out
        #         ahk.send("/{enter}")
        #     if win.active:
        #         ahk.send("/who all \"Legacy of Ik\"{enter}")
        #         time.sleep(3)
