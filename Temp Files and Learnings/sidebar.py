import tkinter as tk

class SideDrawer:
    def __init__(self, master):
        self.master = master
        self.drawer_frame = tk.Frame(self.master, bg='white', width=200, height=400)
        self.drawer_frame.pack(side='left', fill='y')
        self.is_open = False
        
        self.toggle_button = tk.Button(self.master, text='Open Drawer', command=self.toggle_drawer)
        self.toggle_button.pack(side='left', padx=10)
        
    def toggle_drawer(self):
        if not self.is_open:
            self.drawer_frame.pack(side='left', fill='y')
            self.is_open = True
            self.toggle_button.config(text='Close Drawer')
        else:
            self.drawer_frame.pack_forget()
            self.is_open = False
            self.toggle_button.config(text='Open Drawer')

if __name__ == '__main__':
    root = tk.Tk()
    app = SideDrawer(root)
    root.mainloop()
