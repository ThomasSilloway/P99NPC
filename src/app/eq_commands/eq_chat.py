class EQChat:
    def __init__(self, ahk, win):
        self.ahk = ahk
        self.win = win

    def say(self, text):
        self.send_message("/say", text)

    def tell(self, character_name, text):
        self.send_message("/tell " + character_name, text)

    def emote(self, emote_name):
        self.send_command(f"{emote_name}")

    def target(self, player_name):
        self.send_command(f"/target {player_name}")

    def send_message(self, command, text):
        self.send_command(command + " " + text)

    def send_command(self, command):
        self.clear_chat()
        if self.win.active:
            self.ahk.send(command + "{enter}")

    def clear_chat(self):
        if self.win.active:
            # Run who command to make sure text input is cleared out
            self.ahk.send("/{enter}")
