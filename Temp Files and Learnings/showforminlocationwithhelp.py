import tkinter as tk

def show_new_form(event):
    # Create a new form
    form = tk.Toplevel(root)

    # Set the form's width and height
    width = 300
    height = 200

    # Get the button's screen coordinates
    x = event.widget.winfo_rootx()
    y = event.widget.winfo_rooty()

    # Set the location of the form relative to the button
    form.geometry(f"{width}x{height}+{x}+{y}")

# Create the main window
root = tk.Tk()

# Create a button and attach the show_new_form function to its click event
button = tk.Button(root, text="Open Form")
button.bind("<Button-1>", show_new_form)
button.pack()

root.mainloop()
