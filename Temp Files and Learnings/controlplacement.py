import tkinter as tk

root = tk.Tk()

# Using pack()
label = tk.Label(root, text="Enter your name:")
label.pack(side=tk.LEFT)

entry = tk.Entry(root)
entry.pack(side=tk.LEFT, fill=tk.X, expand=True)

button = tk.Button(root, text="Submit")
button.pack(side=tk.RIGHT)

# Using grid()
label.grid(row=0, column=0, sticky=tk.E)

entry.grid(row=0, column=1, sticky=tk.W+tk.E)

button.grid(row=1, column=1, sticky=tk.W)

# Using place()
label.place(x=10, y=10)

entry.place(x=130, y=10, width=200)

button.place(x=350, y=10)

root.mainloop()
