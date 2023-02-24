import tkinter as tk

class CustomTitleBar(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master, bg="#2B2B2B", height=30)

        # Create title bar widgets
        self.close_button = tk.Button(self, text="X", bg="#2B2B2B", fg="#FFFFFF", bd=0, command=self.quit)
        self.title_label = tk.Label(self, text="Custom Title Bar", bg="#2B2B2B", fg="#FFFFFF")

        # Position title bar widgets
        self.close_button.pack(side="right", padx=5)
        self.title_label.pack(side="left", padx=5)

        # Bind mouse events to the title bar
        self.bind("<ButtonPress-1>", self.on_drag_start)
        self.bind("<B1-Motion>", self.on_drag_motion)

    def on_drag_start(self, event):
        self._drag_start_x = event.x
        self._drag_start_y = event.y

    def on_drag_motion(self, event):
        x = self.master.winfo_x() + event.x - self._drag_start_x
        y = self.master.winfo_y() + event.y - self._drag_start_y
        self.master.geometry("+{x}+{y}".format(x=x, y=y))

class CustomBorderlessForm(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)

        # Configure window properties
        self.overrideredirect(True)
        self.geometry("400x300")
        self.configure(bg="#FFFFFF")

        # Create custom title bar
        self.title_bar = CustomTitleBar(self)
        self.title_bar.pack(side="top", fill="x")

        # Add some widgets to the form
        label = tk.Label(self, text="This is a custom borderless form with a title bar.")
        label.pack(padx=50, pady=20)

        button = tk.Button(self, text="Close", command=self.quit)
        button.pack(pady=10)

# Create a new borderless form with a custom title bar
root = tk.Tk()
form = CustomBorderlessForm(root)

# Start the Tkinter event loop
form.mainloop()
