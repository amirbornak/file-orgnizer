import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox



class DirectorySorter:

    
    def __init__(self, root):
        self.root = root
        self.root.title("Directory Sorter")
        
        self.label = tk.Label(root, text="Select a directory to sort:")
        self.label.pack(pady=10)
        
        self.button = tk.Button(root, text="Browse", command=self.browse_directory)
        self.button.pack(pady=5)
        
        self.status = tk.Label(root, text="", fg="green")
        self.status.pack(pady=10)
    

    def browse_directory(self):
        self.path = filedialog.askdirectory()
        if self.path:
            self.sort_directory(self.path)
            self.status.config(text=f"Files in '{self.path}' have been sorted.")
        else:
            self.status.config(text="No directory selected.", fg="red")
    

    def sort_directory(self, path):
        list_ = os.listdir(path)
        
        for file_ in list_:
            file_path = os.path.join(path, file_)
            if os.path.isdir(file_path):
                continue
            
            name, ext = os.path.splitext(file_)
            ext = ext[1:]
            if ext == '':
                ext = 'no_extension'
            
            destination_dir = os.path.join(path, ext)
            if not os.path.exists(destination_dir):
                os.makedirs(destination_dir)
            
            shutil.move(file_path, os.path.join(destination_dir, file_))



if __name__ == "__main__":
    root = tk.Tk()
    app = DirectorySorter(root)
    root.mainloop()