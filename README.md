DirectorySorter
Overview
DirectorySorter is a user-friendly Python application designed using Tkinter to help you effectively organize files within a specified directory by their file extensions. The tool automatically creates subdirectories for each file type, allowing you to maintain a tidy digital workspace.

Features
User-friendly GUI: An intuitive graphical interface that simplifies navigation.
Directory Selection: Easily browse and select the directory you wish to sort.
Automatic Sorting: Files are sorted automatically into subdirectories based on their extensions.
Extension Handling: Files without extensions are moved into a dedicated “no_extension” folder.
Requirements
To run this application, ensure you have the following packages installed:

Python 3.x
Tkinter (typically included with Python installations)
Additionally, you may need to install the shutil module if it’s not already available:

pip install shutil
        
    
Installation
Clone or download the repository to your local machine.

Navigate to the project directory.

Run the script using Python:

python main.py
        
    
Usage
Launch the application.
Click the Browse button to select the directory you want to sort.
After selecting a directory, the application will automatically sort all files into subdirectories based on their extensions.
Check the status message for confirmation that sorting has been completed.
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
        
    
Contributing
We welcome contributions to this project! Feel free to fork the repository and submit a pull request.

Tags
Python
Tkinter
File Management
Sorting
GUI
Open Source
GNU License
License
This project is open-source and available under the GNU GENERAL PUBLIC LICENSE.

Author
Developed by amirbornak here.
