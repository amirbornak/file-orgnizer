# Directory Sorter

## Overview

The Directory Sorter is a simple Python application that helps users organize files within a specified directory by sorting them into subdirectories based on their file extensions. This tool utilizes Tkinter for a user-friendly graphical interface, making it easy to select a directory and sort files with just a few clicks.

## Features

- **Interactive GUI**: Built using Tkinter, the application provides a straightforward interface for selecting directories.
- **Automatic Sorting**: Files are automatically sorted into subdirectories named after their extensions.
- **Error Handling**: User feedback is displayed regarding the sorting process, ensuring clarity on actions taken.

## Requirements

- Python 3.x
- Tkinter (usually included with Python installations)
  
## Installation

1. Clone the repository or download the script.
2. Ensure you have Python installed on your system.
3. Run the application:

   ```bash
   python directory_sorter.py

Usage
1) Launch the application. 
   A window titled “Directory Sorter” will appear.
2) Click on the “Browse” button to select the directory you want to sort.

The application will process the files and create subdirectories based on their extensions.
After sorting, a message will indicate that the files have been sorted successfully.

How It Works
1. The application scans the selected directory for files.
2. It identifies the file extension for each file.
3. If a subdirectory for a specific extension doesn’t exist, it creates one.
4. Files are then moved into their corresponding subdirectory based on the extension.

Example
If your directory contains the following files:

image1.jpg
document1.pdf
script1.py
notes.txt
image2.png


After running the sorter, the directory would look like:

/your_directory/
    /jpg/
        image1.jpg
    /pdf/
        document1.pdf
    /py/
        script1.py
    /txt/
        notes.txt
    /png/
        image2.png


Contributing
Feel free to submit issues or pull requests if you have suggestions for improvements or fixes!

License
This project is licensed under the GNU General Public License (GNU GPL or simply GPL)

Author

Created with love by amirbornak 


