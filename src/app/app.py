import time
from ahk import AHK


class App:

    def run(self):
        window_name = b"WinEQ 2.15 WinEQ2-EQ 2.15 - EverQuest (Hotkey: Ctrl+Alt+1)"
        ahk = AHK()
        # for window in ahk.windows():
        #     print(window.title)
        #     print(window.process)

        # window_name = b'Strawberry'
        # window_name = b'Untitled - Notepad'
        # window_name = b'EverQuest'

        win = ahk.find_window(title=window_name)
        win.activate()

        time.sleep(0.1)
        # win.send("1")
        # win.move(x=200, y=300, width=500, height=800)
        ahk.mouse_move(x=800, y=400, speed=5)
        # Run who command
        while True:
            if win.active:
                # Run who command to make sure text input is cleared out
                ahk.send("/{enter}")
                ahk.send("/who all \"Legacy of Ik\"{enter}")
                time.sleep(3)
        # ahk.type("1")
        # ahk.key_press("i")
        # ahk.send_input("i")
        # ahk.key_down("w")
        # time.sleep(0.5)
        # ahk.key_up("w")

        # ahk.show_tooltip("This is a friendly tooltip? ", second=2, x=800, y=400)  # ToolTip
        # for window in ahk.windows():
        #     print(window.title)
        #     print(window.process)
