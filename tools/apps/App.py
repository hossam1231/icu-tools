# Sure, here's an annotated explanation of each line of code in the provided Python script:
from tkinter import Text, Scrollbar
# Import necessary modules
import subprocess  # Allows running external commands
import curses      # Library for creating console-based UIs
import json        # Library for handling JSON data
import main_script  # Replace with the actual path to your main script
import tkinter as tk

def run_selected_apps(selected_apps):
    apps_data = read_apps_from_json()  # Read app data from a JSON file

    for app_index in selected_apps:  # Loop through selected app indices
        if 0 <= app_index < len(apps_data):  # Check if the app index is valid
            app = apps_data[app_index]  # Get the app data
            main_script.app_selector.start_new_process(app['name'], f"python3 apps/{app['file']}")

# Function to read the list of apps from a JSON file
def read_apps_from_json():
    try:
        # Open and read the "apps.json" file
        with open("apps.json", "r") as json_file:
            apps_data = json.load(json_file)  # Parse JSON data from the file
        return apps_data  # Return the parsed data
    except FileNotFoundError:
        return []  # Return an empty list if the file is not found

# Function to write the list of apps to a JSON file
def write_apps_to_json(apps_data):
    with open("apps.json", "w") as json_file:
        json.dump(apps_data, json_file, indent=4)  # Serialize data to JSON format and write it to the file with indentation

# Define a function to list apps in the console UI
def list_apps(stdscr, selected_apps, current_selection):
    stdscr.clear()  # Clear the console screen
    height, width = stdscr.getmaxyx()  # Get the height and width of the console window

    # Title and welcome message
    title = "ICU Apps"
    welcome_message = "Welcome to our apps!"
    stdscr.addstr(1, width // 2 - len(title) // 2, title, curses.A_BOLD)  # Print the title at the center of the screen
    stdscr.addstr(3, width // 2 - len(welcome_message) // 2, welcome_message)  # Print a welcome message

    apps_data = read_apps_from_json()  # Read app data from a JSON file

    # Instructions
    instructions = "Use arrow keys to navigate, press 'Space' to toggle selection, 'Enter' to run selected apps, and 'q' to quit."
    stdscr.addstr(height - 2, 1, instructions, curses.A_BOLD)  # Print instructions at the bottom of the screen

    for index, app in enumerate(apps_data):  # Loop through the list of apps
        x = width // 4
        y = 6 + index * 2  # Calculate the y-coordinate for each app entry

        is_selected = index in selected_apps  # Check if the app is selected
        if index == current_selection:
            stdscr.attron(curses.color_pair(1))  # Highlight the selected app
            stdscr.addstr(y, x, " [X]" if is_selected else " [ ]")  # Print a checkbox for selection
            stdscr.addstr(y, x + 6, app['name'])  # Print the app name
            stdscr.addstr(y + 1, x + 6, "- " + app['description'])  # Print the app description
            stdscr.attroff(curses.color_pair(1))  # Turn off the highlighting
        else:
            stdscr.addstr(y, x, " [X]" if is_selected else " [ ]")  # Print a checkbox for selection
            stdscr.addstr(y, x + 6, app['name'])  # Print the app name

    stdscr.refresh()  # Refresh the console screen to display changes

# Define the main function
def main(stdscr):
    # ...
    global root
    root = tk.Tk()  # Create a Tkinter root window
    root.withdraw()  # Hide the root window
    main_script.app_selector = main_script.AppSelector(root)
    curses.curs_set(0)  # Hide the cursor
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)  # Initialize a color pair for highlighting

    selected_apps = set()  # Use a set to store selected app indices
    current_selection = 0  # Initialize the current selection index

    while True:
        list_apps(stdscr, selected_apps, current_selection)  # Display the list of apps
        key = stdscr.getch()  # Get a keyboard input

        if key == ord('q'):  # If 'q' is pressed, exit the program
            break
        elif key == curses.KEY_DOWN:  # If the down arrow key is pressed, move the selection down
            current_selection = min(len(read_apps_from_json()) - 1, current_selection + 1)
        elif key == curses.KEY_UP:  # If the up arrow key is pressed, move the selection up
            current_selection = max(0, current_selection - 1)
        elif key == 32:  # If the Space key is pressed, toggle app selection
            selected_app_index = current_selection
            if selected_app_index in selected_apps:
                selected_apps.remove(selected_app_index)  # Deselect the app
            else:
                selected_apps.add(selected_app_index)  # Select the app
        elif key == 10:  # If the Enter key is pressed, run selected apps
            run_selected_apps(selected_apps)

if __name__ == "__main__":
    curses.wrapper(main)  # Initialize the curses library and run the main function

# This code defines a console-based application for selecting and running apps listed in a JSON file, and it uses the curses library for creating a simple text-based user interface. The code is well-commented to explain each part of the program.