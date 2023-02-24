import tkinter as tk

root = tk.Tk()

# Set the width and height of the form
width = 300
height = 200

# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate the x and y coordinates for the top-left corner of the form
x = (screen_width // 2) - (width // 2)
y = (screen_height // 2) - (height // 2)

# Set the geometry of the form
root.geometry(f"{width}x{height}+{x}+{y}")

root.mainloop()
