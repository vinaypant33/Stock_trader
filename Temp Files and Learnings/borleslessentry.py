import tkinter as tk

root = tk.Tk()

# Create an Entry widget with no border and no highlight thickness
entry = tk.Entry(root, bd=0, highlightthickness=0)
entry.pack(pady=20)

root.mainloop()
