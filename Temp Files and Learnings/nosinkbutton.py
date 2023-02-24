import tkinter as tk

class CustomButton(tk.Button):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.config(relief=tk.FLAT, bd=0, highlightthickness=0)

    def invoke(self):
        # override the invoke method to prevent click effect
        pass

if __name__ == '__main__':
    root = tk.Tk()

    button = CustomButton(root, text="Click me!")
    button.pack(padx=50, pady=50)

    root.mainloop()
