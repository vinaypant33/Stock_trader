### Importing the pre made modules
import tkinter as tk
from tkinter import messagebox



## Login Screen Started 
class LoginScreen():

    def __init__(self) -> None:
        self.loginscreen = tk.Tk
        # self.loginscreen.overrideredirect(True)
        self.height  = self.loginscreen.winfo_screenheight(self)
        self.width  = self.loginscreen.winfo_screenwidth(self)

        messagebox.showinfo("sdfsdf" , self.width)

    

## Login Screen Ended 





if __name__ == '__main__':
    name  = LoginScreen()
    