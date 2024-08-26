# DirectorySorter

## Overview

`DirectorySorter` is a simple Python application built with Tkinter that allows users to organize files in a selected directory by their file extensions. This tool automatically creates subdirectories for each file type and moves the corresponding files into their respective folders, helping to keep your directories tidy.

## Features

- **User-friendly GUI**: The application provides a graphical interface for easy navigation.
- **Directory Selection**: Users can browse and select a directory to sort.
- **Automatic Sorting**: Files are automatically sorted into subdirectories based on their file extensions.
- **Extension Handling**: Files without extensions are moved into a dedicated "no_extension" folder.

## Requirements

To run this application, ensure you have the following packages installed:

- Python 3.x
- Tkinter (usually included with Python installations)

You may also need to install the `shutil` module if it is not available:

```bash
pip install shutil

Installation
Clone or download the repository to your local machine.
Navigate to the project directory.
Run the script using Python:
python main.py
----------------------------------------------------------------------------------------------------------------
Usage
Launch the application.
Click the Browse button to select the directory you want to sort.
Once a directory is selected, the application will sort all files into subdirectories based on their extensions.
Check the status message for sorting confirmation.

----------------------------------------------------------------------------------------------------------------
Example Directory Structure

/your_directory
    ├── document.txt
    ├── image.png
    ├── script.py
    ├── audio.mp3
    ├── no_extension
    └── /text
        └── document.txt
    └── /image
        └── image.png
    └── /audio
        └── audio.mp3

-------------------------------------------------------------------------------------------------------------

Contributing
If you would like to contribute to this project, feel free to fork the repository and submit a pull request.

-------------------------------------------------------------------------------------------------------------

Tags
Python
Tkinter
File Management
Sort
GUI
Open Source
GNU License
-------------------------------------------------------------------------------------------------------------

License
This project is open-source and available under GNU GENERAL PUBLIC LICENSE.
Author
Developed by [https://github.com/amirbornak].

Feel free to replace the placeholder for the author section with your name or GitHub handle!