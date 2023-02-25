import tkinter as tk

root = tk.Tk()

# Create a font object with a larger size
large_font = ('Arial', 16)

# Create an Entry widget with a larger font and size
entry = tk.Entry(root, font=large_font, width=30)
entry.pack(pady=20)

root.mainloop()
