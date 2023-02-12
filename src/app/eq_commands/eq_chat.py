class EQChat:
    def __init__(self, ahk, win):
        self.ahk = ahk
        self.win = win

    def say(self, text):
        self.send_message("/say", text)

    def tell(self, character_name, text):
        self.send_message("/tell " + character_name, text)

    def send_message(self, command, text):
        self.clear_chat()
        self.ahk.send(command + " " + text + "{enter}")

    def clear_chat(self):
        if self.win.active:
            # Run who command to make sure text input is cleared out
            self.ahk.send("/{enter}")
