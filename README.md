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

## Usage

1. **Launch the Application**: Open the terminal or command prompt and run the script. A window titled **“Directory Sorter”** will appear.
2. **Select Directory**: Click on the **“Browse”** button to choose the directory you want to sort.
3. **Sorting Process**: The application will scan the selected directory, process the files, and create subdirectories based on their extensions.
4. **Completion Message**: Once sorting is complete, a message will appear indicating that the files have been sorted successfully.

## How It Works

1. **Directory Scan**: The application scans the selected directory for files.
2. **Extension Identification**: It identifies the file extension for each file.
3. **Subdirectory Creation**: If a subdirectory for a specific extension doesn’t already exist, it creates one.
4. **File Movement**: Files are then moved into their corresponding subdirectory based on their extension.

## Example

If your directory contains the following files:
image1.jpg document1.pdf script1.py notes.txt image2.png

After running the sorter, the directory will be organized as follows:


your_directory/
├── jpg/
│   └── image1.jpg
├── pdf/
│   └── document1.pdf
├── py/
│   └── script1.py
├── txt/
│   └── notes.txt
└── png/
    └── image2.png

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests if you have suggestions for improvements or fixes. 

## License

This project is licensed under the GNU License. 

## Author

Created with love by amirbornak
