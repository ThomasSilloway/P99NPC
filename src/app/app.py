import time
from ahk import AHK


class App:

    def __init__(self, config):
        self.config = config

    def run(self):
        window_name = self.config.get("eq_window_name")
        ahk = AHK()
        # for window in ahk.windows():
        #     print(window.title)
        #     print(window.process)

        win = ahk.find_window(title=window_name.encode())
        win.activate()

        time.sleep(0.1)
        # win.send("1")
        # win.move(x=200, y=300, width=500, height=800)
        # ahk.mouse_move(x=800, y=400, speed=5)
        # Run who command
        while True:
            if win.active:
                # Run who command to make sure text input is cleared out
                ahk.send("/{enter}")
            if win.active:
                ahk.send("/who all \"Legacy of Ik\"{enter}")
                time.sleep(3)
        # ahk.type("1")
        # ahk.key_press("i")
        # ahk.send_input("i")
        # ahk.key_down("w")
        # time.sleep(0.5)
        # ahk.key_up("w")

        # ahk.show_tooltip("This is a friendly tooltip? ", second=2, x=800, y=400)  # ToolTip
