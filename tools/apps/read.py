import os
import time
from gitignore_parser import parse_gitignore

folder_path = "/path/to/your/folder"
folders_to_ignore = ["node_modules", "folder_to_ignore2"]

def is_ignored(file_path, gitignore):
    # Check if the file is matched by the .gitignore patterns
    return gitignore(file_path)

def read_and_log_files(folder_path):
    try:
        gitignore = None

        # Look for .gitignore files two levels above the current directory
        for _ in range(2):
            folder_path = os.path.dirname(folder_path)

        gitignore_path = os.path.join(folder_path, ".gitignore")

        if os.path.exists(gitignore_path):
            # Parse the .gitignore file
            gitignore = parse_gitignore(gitignore_path)

        while True:
            for root, dirs, files in os.walk(folder_path, topdown=True):
                # Exclude folders listed in folders_to_ignore
                dirs[:] = [d for d in dirs if d not in folders_to_ignore]

                for file_name in files:
                    file_path = os.path.join(root, file_name)

                    # Check if it's a file (not a directory)
                    if os.path.isfile(file_path):
                        try:
                            # Check if the file is ignored by .gitignore
                            if gitignore is None or not is_ignored(file_path, gitignore):
                                with open(file_path, 'r') as file:
                                    file_contents = file.read()
                                print(f"Contents of {file_path}:\n{file_contents}\n")
                            else:
                                print(f"Ignored file: {file_path}\n")

                        except Exception as e:
                            print(f"Error reading {file_path}: {str(e)}")

            # Sleep for a while before checking again
            time.sleep(1)

    except KeyboardInterrupt:
        print("Exiting...")

if __name__ == "__main__":
    read_and_log_files(folder_path)
