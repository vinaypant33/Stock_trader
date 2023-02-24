import tkinter as tk

class HoverButton(tk.Button):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.default_bg = self["background"]
        self.hover_bg = "light blue"

        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, event):
        self.config(background=self.hover_bg)

    def on_leave(self, event):
        self.config(background=self.default_bg)

if __name__ == '__main__':
    root = tk.Tk()

    button = HoverButton(root, text="Hover over me!")
    button.pack(padx=50, pady=50)

    root.mainloop()
