import subprocess
import socket
import tkinter as tk

def get_interfaces():
    interfaces = []
    try:
        output = subprocess.check_output(["ifconfig"])
        output = output.decode("utf-8")
        lines = output.split("\n")
        for line in lines:
            if line.startswith("en") or line.startswith("eth"):
                interface = line.split(":")[0]
                interfaces.append(interface)
    except subprocess.CalledProcessError:
        print("Failed to retrieve network interfaces.")
    return interfaces

def get_mac(interface):
    try:
        output = subprocess.check_output(["ifconfig", interface])
        output = output.decode("utf-8")
        lines = output.split("\n")
        for line in lines:
            if "ether" in line:
                mac_address = line.split("ether")[1].strip()
                return mac_address
    except subprocess.CalledProcessError:
        print(f"Failed to retrieve MAC address for {interface}.")
    return None

def set_mac():
    try:
        process = subprocess.Popen(['sh', 'randoMac.sh'], shell=False, stdin=subprocess.PIPE, stdout=subprocess.PIPE)

        for line in process.stdout:
                    output = line.decode("utf-8").strip()  # Decode and strip each line of output from the subprocess
                    print(output)  # Print the output
       
        process.stdin.write(b'\n')  # Send an empty string as input
        process.stdin.flush()  # Flush the input buffer
    except subprocess.CalledProcessError as e:
        print(f"Failed to set MAC address: {e}")


def create_gui():
    window = tk.Tk()
    window.title("MAC Address Changer")

    adapter_label = tk.Label(window, text="Adapter:")
    adapter_label.pack()
    interfaces = get_interfaces()
    if not interfaces:
        print("No network interfaces found.")
        return

    adapter_var = tk.StringVar(window)
    adapter_var.set(interfaces[0])  # Set the default adapter
    adapter_dropdown = tk.OptionMenu(window, adapter_var, *interfaces)
    adapter_dropdown.pack()

    set_mac_button = tk.Button(window, text="Random MAC Address", command=set_mac)
    set_mac_button.pack()

    interfaces = get_interfaces()
    if not interfaces:
        print("No network interfaces found.")
        return

    for interface in interfaces:
        mac_address = get_mac(interface)
        if mac_address:
            label = tk.Label(window, text=f"{interface}:")
            label.pack()
            value = tk.Label(window, text=mac_address)
            value.pack()

    window.mainloop()

create_gui()