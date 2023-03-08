import tkinter as tk

class DrawerForm:
    def __init__(self, master):
        self.master = master
        self.drawer_width = 200
        self.drawer_frame = tk.Frame(self.master, bg='white', width=self.drawer_width, height=400)
        self.drawer_frame.pack(side='left', fill='y')
        self.is_open = False
        
        self.main_frame = tk.Frame(self.master)
        self.main_frame.pack(side='left', fill='both', expand=True)
        
        self.toggle_button = tk.Button(self.main_frame, text='Open Drawer', command=self.toggle_drawer)
        self.toggle_button.pack(side='top', pady=10)
        
    def toggle_drawer(self):
        if not self.is_open:
            self.drawer_frame.pack(side='left', fill='y')
            self.master.geometry(f'{self.master.winfo_width() + self.drawer_width}x{self.master.winfo_height()}')
            self.is_open = True
            self.toggle_button.config(text='Close Drawer')
        else:
            self.drawer_frame.pack_forget()
            self.master.geometry(f'{self.master.winfo_width() - self.drawer_width}x{self.master.winfo_height()}')
            self.is_open = False
            self.toggle_button.config(text='Open Drawer')

if __name__ == '__main__':
    root = tk.Tk()
    app = DrawerForm(root)
    root.mainloop()
