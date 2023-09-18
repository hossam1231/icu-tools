import tkinter as tk
from tkinter import messagebox
import subprocess
from subprocess import Popen, PIPE
from tkinter import simpledialog
import threading


# decorator
def run_once(func):
    def wrapper(*args, **kwargs):
        if not wrapper.has_run:
            wrapper.has_run = True
            return func(*args, **kwargs)
    wrapper.has_run = False
    return wrapper

def shell_with_sudo(sudo_command):
    process = Popen(sudo_command, shell=True, stdout=PIPE, stderr=PIPE)
    stdout, stderr = process.communicate()
    
    output = stdout.decode().strip()
    print(output)  # Print the output to the console
    
    return output


# Create a lock object
command_lock = threading.Lock()

# Flag variable to track if the script has already been executed
script_executed = False



def run_command_with_sudo(command):
    # Acquire the lock
    command_lock.acquire()
        # Ask for the sudo password using a text input dialog
    password = simpledialog.askstring("Sudo Password", "Enter your sudo password:", show='*')
        # Construct the sudo command with the provided password
    sudo_command = f"echo '{password}' | sudo -S {command}"
        # Release the lock
    command_lock.release() 
    # Execute the sudo command
    shell_with_sudo(sudo_command)

# 
def run_randoMac_script():
    global script_executed
    if not script_executed:
        script_path = "./randoMac.sh"
        run_command_with_sudo(f"sh {script_path}  && en0")
        script_executed = True

def run_script():
    choice = choice_var.get()

    if choice == 1:
        run_randoMac_script()
        root.destroy()
    elif choice == 2:
        root.destroy()
    else:
        messagebox.showerror("Error", "Invalid choice. Please try again.")
    
    


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Wifi buster")
    root.geometry("300x200")

    choice_var = tk.IntVar()

    label = tk.Label(root, text="Select an option:")
    label.pack()

    radio_button1 = tk.Radiobutton(root, text="Start wifi buster", variable=choice_var, value=1)
    radio_button1.pack()

    radio_button2 = tk.Radiobutton(root, text="Exit", variable=choice_var, value=2)
    radio_button2.pack()

    button = tk.Button(root, text="Continue", command=run_script)
    button.pack()


    root.mainloop()