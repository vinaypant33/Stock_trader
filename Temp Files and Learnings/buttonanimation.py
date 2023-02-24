import tkinter as tk

class AnimatedButton(tk.Button):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.colors = ["red", "orange", "yellow", "green", "blue", "purple"]
        self.color_index = 0

        self.animate()

    def animate(self):
        self.config(bg=self.colors[self.color_index])
        self.color_index = (self.color_index + 1) % len(self.colors)
        self.after(500, self.animate)

if __name__ == '__main__':
    root = tk.Tk()

    button = AnimatedButton(root, text="Click me!")
    button.pack(padx=50, pady=50)

    root.mainloop()
