# Importing Pre made modules
import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import *  

# Importing Project made modules
import colors
import fonts



class Dashboard():

    def __init__(self) -> None:
        self.dashboard = tk.Tk()
        self.dashboard.overrideredirect(True)
        self.screen_height  = self.dashboard.winfo_screenheight()
        self.screen_width = self.dashboard.winfo_screenwidth()
        self.height  = 700
        self.width  = 1000
        self.ycoordinate  = (self.screen_height //2 ) - (self.height //2 )
        self.xcoordinate  = ( self.screen_width //2 )  -  (self.width //2 )
        self.dashboard.geometry(f"{self.width}x{self.height}+{10}+{20}")

    ## Functions for the general work 
    def closing_app(self):
        self.dashboard.destroy()
    
    def mouse_move(self, event):
        self.x = event.x
        self.y = event.y
    
    def move_window(self , event):
        self.deltax = event.x - self.x
        self.deltay = event.y - self.y
        self.newx  = self.dashboard.winfo_x() + self.deltax
        self.newy = self.dashboard.winfo_y() + self.deltay
        self.dashboard.geometry(f"{self.width}x{self.height}+{self.newx}+{self.newy}")

    def defining_controls(self):
        ## Defining frames - for the controls
        self.dashboard.configure(background=colors.white_backgrond)
        self.control_frame = tk.Frame(self.dashboard  , border=0  ,background=colors.dark_grey)
        self.control_frame.bind("<ButtonPress-1>" , self.mouse_move)
        self.control_frame.bind("<B1-Motion>" , self.move_window)
        self.control_button  = tk.Button(self.control_frame , text=" X " , foreground=colors.color_red , background=colors.dark_grey  , 
                                         relief=tk.FLAT , border=0 , activebackground=colors.color_red ,activeforeground=colors.white_backgrond , command=self.closing_app)
        
        self.control_frame.propagate(1)

       ### Defining the sidebar from here 
        self.sidebar = tk.Frame(self.dashboard , background=colors.sky_blue, width=150 , height=676)
        self.sidebar.pack_propagate(1)
        #### Width 100 and height 676 would be chnaged in the main function and also
        
        self.home_button  = tk.Button(self.sidebar , text="Home")
        self.settings_button  =tk.Button(self.sidebar , text="Settings")
        self.history_button = tk.Button(self.sidebar , text="History")



        

        



    def placing_controls(self):
        self.control_frame.pack(side='top' , pady=0 , fill='x')
        self.control_button.pack(side='right' , padx=0 , pady=1)
        # self.sidebar.pack(side="left" , fill="y")
        self.sidebar.place(x=0 , y=24)

        self.home_button.place(x=0,y=100)
        self.settings_button.place(x = 10 , y = 10)
        self.history_button.place(x = 0 , y=100)


        # Calling the main app
        self.dashboard.mainloop()





if __name__ == '__main__':
    hehe = Dashboard()
    hehe.defining_controls()
    hehe.placing_controls()

        
