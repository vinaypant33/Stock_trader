import tkinter as tk

root = tk.Tk()

def on_button_click():
    print("Button clicked")

# Create a button with a fixed color
button = tk.Button(root, text="Click Me", bg="#2B2B2B", fg="#FFFFFF", activebackground="#2B2B2B", highlightbackground="#2B2B2B", command=on_button_click)
button.pack(pady=20)

root.mainloop()
