import tkinter as tk

class BorderlessWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        self.overrideredirect(True)  # remove title bar and borders
        self.geometry("200x200")  # set initial size

        # bind events to allow the window to be moved
        self.bind("<ButtonPress-1>", self.start_move)
        self.bind("<B1-Motion>", self.move_window)

    def start_move(self, event):
        self.x = event.x
        self.y = event.y

    def move_window(self, event):
        deltax = event.x - self.x
        deltay = event.y - self.y
        new_x = self.winfo_x() + deltax
        new_y = self.winfo_y() + deltay
        self.geometry(f"+{new_x}+{new_y}")

if __name__ == '__main__':
    app = BorderlessWindow()
    app.mainloop()
