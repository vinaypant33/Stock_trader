import tkinter as tk
from tkinter import messagebox
from pubsub import pub


## Class for the Custom Messagebox
class Messagebox():

    # Init function for all the initial description and calls
    def __init__(self , height , width , xlocation , ylocation , *text) -> None:
        self.messagebox  = tk.Tk()
        self.messagebox.overrideredirect(True)
        self.height  = height
        self.width  = width
        self.x  = xlocation
        self.y  = ylocation
        self.messagebox.geometry(f"{width}x{height}+{xlocation}+{ylocation}")

    #### Function for the min app 
    def closing_form(self):
        self.closing_messagebox()

    def start_move(self, event):
        self.x = event.x
        self.y = event.y

    def move_window(self, event):
        deltax = event.x - self.x
        deltay = event.y - self.y
        new_x = self.messagebox.winfo_x() + deltax
        new_y = self.messagebox.winfo_y() + deltay
        self.messagebox.geometry(f"{self.width}x{self.height}+{new_x}+{new_y}")

    #### Function calling Completed
    def defining_controls(self):
        self.messagebox.config(background='white')
        self.upperframe = tk.Frame(self.messagebox , background='#040F16' , height=40)
        self.upperframe.pack_propagate(True)
        self.close_button = tk.Button(self.upperframe , text='X' , relief=tk.FLAT , bd=0 , 
        highlightthickness=0 , background='#040F16' , activebackground= '#040F16'  , activeforeground= 'red', foreground='red' , command=self.closing_form)
        self.text = tk.Label(self.messagebox , foreground='black' , background='white' , text="Please Enter the values in the data sheet ")
        ### Control Binding done here  S
        self.upperframe.bind("<ButtonPress-1>" , self.start_move)
        self.upperframe.bind("<B1-Motion>"  ,self.move_window)

    def placing_controls(self):
        self.upperframe.pack(side="top" , fill="x" )
        self.close_button.pack(side='right' , padx=4)
        self.text.pack(side='left' , padx=15 , fill=tk.BOTH)

    def calling_controls(self):
        self.messagebox.mainloop()

    def closing_messagebox(self):
        self.messagebox.destroy()

## Custom Messagebox Ended

if __name__ == '__main__':
    custombox  = Messagebox(height=300 , width=500 ,xlocation=100 , ylocation=100)
    custombox.defining_controls()
    custombox.placing_controls()
    custombox.calling_controls()

