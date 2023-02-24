import tkinter as tk

class CustomMessageBox:
    def __init__(self, parent, title, message):
        self.top = tk.Toplevel(parent)
        self.top.title(title)

        label = tk.Label(self.top, text=message)
        label.pack(padx=20, pady=20)

        ok_button = tk.Button(self.top, text="OK", command=self.ok)
        ok_button.pack(pady=10)

    def ok(self):
        self.top.destroy()

if __name__ == '__main__':
    root = tk.Tk()

    message_box = CustomMessageBox(root, "Custom Message Box", "This is a custom message box.")
    root.wait_window(message_box.top)

    root.mainloop()
