from tkinter import filedialog
import tkinter as tk

# Create a function to open the file dialog
def open_file_dialog():
    file_path = filedialog.askopenfilename()
    # Do something with the selected file path (e.g., display it)
    file_label.config(text="Selected File: " + file_path)

# Create the main window
root = tk.Tk()
root.title("File Browser Example")

# Create a button to open the file dialog
open_button = tk.Button(root, text="Open File", command=open_file_dialog)
open_button.pack()

# Create a label to display the selected file path
file_label = tk.Label(root, text="Selected File: ")
file_label.pack()

# Start the main event loop
root.mainloop()