#!/bin/bash

# Get the currently logged-in username
username="$USER"

# Specify the font folder path
font_folder="."

# Check if the font folder exists
if [ -d "$font_folder" ]; then
    # Iterate through the font files in the directory
    for font_file in "$font_folder"/*.otf; do
        if [ -f "$font_file" ]; then
            # Copy the font file to the user's Fonts folder
            cp -R "$font_file" "/Users/$username/Library/Fonts/"
            
            # Check if the copy operation was successful
            if [ $? -eq 0 ]; then
                echo "Font '$font_file' installed for user '$username'."
            else
                echo "Failed to install font '$font_file' for user '$username'."
            fi
        fi
    done
else
    echo "Font folder '$font_folder' not found."
fi
