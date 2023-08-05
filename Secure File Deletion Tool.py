import os
import random
import string
import tkinter as tk
from tkinter import filedialog

class SecureFileDeletionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Secure File Deletion Tool")
        
        self.label = tk.Label(root, text="Select a file to securely delete:")
        self.label.pack(pady=10)
        
        self.select_button = tk.Button(root, text="Select File", command=self.select_file)
        self.select_button.pack(pady=5)
        
        self.delete_button = tk.Button(root, text="Securely Delete", command=self.securely_delete)
        self.delete_button.pack(pady=5)
        
        self.file_path = ""

    def select_file(self):
        self.file_path = filedialog.askopenfilename()
    
    def securely_delete(self):
        if self.file_path:
            try:
                with open(self.file_path, 'wb') as file:
                    file_size = os.path.getsize(self.file_path)
                    for _ in range(file_size):
                        file.write(bytes([random.randint(0, 255)]))
                
                result_label.config(text=f"File '{os.path.basename(self.file_path)}' securely deleted.")
            except Exception as e:
                result_label.config(text=f"An error occurred: {e}")
        else:
            result_label.config(text="Please select a file to securely delete.")
        

if __name__ == "__main__":
    root = tk.Tk()
    app = SecureFileDeletionApp(root)
    
    result_label = tk.Label(root, text="", fg="green")
    result_label.pack(pady=10)
    
    root.mainloop()
