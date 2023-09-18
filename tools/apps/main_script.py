import tkinter as tk
from tkinter import Text, Scrollbar
import subprocess
import threading

class ProcessWindow:
    def __init__(self, root, custom_name, process_command):
        self.root = root
        self.custom_name = custom_name
        self.process_command = process_command

        self.text = Text(root, wrap=tk.WORD)
        self.text.pack(fill=tk.BOTH, expand=True)

        self.scrollbar = Scrollbar(root)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.text.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.text.yview)

        self.process = None

    def start_process(self):
        self.process = subprocess.Popen(
            self.process_command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=True,
            text=True,
            bufsize=1,
            universal_newlines=True,
        )
        threading.Thread(target=self.read_output).start()

    def read_output(self):
        while True:
            line = self.process.stdout.readline()
            if not line:
                break
            self.update_text(line)

    def update_text(self, line):
        self.text.insert(tk.END, line)
        self.text.see(tk.END)

    def stop_process(self):
        if self.process:
            self.process.terminate()

class AppSelector:
    def __init__(self, root):
        self.root = root
        self.root.title("App Selector")

        # Create a button to start a new process window
        start_button = tk.Button(root, text="Start Process", command=self.start_new_process)
        start_button.pack()

    def start_new_process(self, custom_name, app_command):
        if app_command:
            root = tk.Toplevel(self.root)
            window = ProcessWindow(root, custom_name, app_command.split())
            window.start_process()

if __name__ == "__main__":
    root = tk.Tk()
    app_selector = AppSelector(root)
    root.mainloop()