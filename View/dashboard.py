# Importing Pre made modules
import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import *  
from PIL import Image, ImageTk

# Importing Project made modules
import colors
import fonts
import assets



#### Constants : for the active control and other fixed parts
## Current page 



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

        # Defining Constants 
        self.sidebar_maximized  =  True

        # Importing the image files 
        home_image  = Image.open(r"View\home.png")
        home_resized  = home_image.resize((1000 ,1000))
        self.home_final_image  = ImageTk.PhotoImage(home_resized)


        

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

    ## Functions for hovering Part
    def open_close_hover_enter(self, event):
        self.open_close_button.configure(background=colors.avatar_background)
    
    def open_close_hover_close(self, event):
        self.open_close_button.configure(background=colors.black_color)
    
    def home_button_enter(self, event):
        self.home_button.configure(background=colors.sky_blue)
    
    def home_button_leave(self, enter):
        self.home_button.configure(background=colors.color_red)
    
    def settings_button_enter(self, event):
        self.settings_button.configure(background=colors.sky_blue)
    
    def settings_button_leave(self, event):
        self.settings_button.configure(background=colors.color_red)

    def history_button_enter(self, event):
        self.history_button.configure(background=colors.sky_blue)
    
    def history_button_leave(self , event):
        self.history_button.configure(background=colors.color_red)

    # Function to maximize and minimize the sidebar
    def sidebar_max_min(self):
        if self.sidebar_maximized == False:
            self.sidebar.configure(width=150)
            self.sidebar_maximized = True
            self.open_close_button.place(x =111 , y = 2)
            self.home_button.configure(width=16 ,  image=self.home_final_image)
            self.settings_button.configure(width=16)
            self.history_button.config(width=16)
            
        elif self.sidebar_maximized == True:
            self.sidebar_maximized = False
            self.sidebar.configure(width=71)
            self.open_close_button.place(x=30 , y=2 )
            # self.home_button.config(width=7)
            
            self.settings_button.config(width=7)
            self.history_button.config(width=7)

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
        self.sidebar.pack_propagate(0)

        #### Width 100 and height 676 would be chnaged in the main function and also
        self.open_close_button   =tk.Button(self.sidebar , text="+==+" , bd = 0 , activebackground=colors.sky_blue , activeforeground=colors.white_backgrond , foreground=colors.color_red , background=colors.dark_grey , height=1 , command=self.sidebar_max_min)
        self.home_button  = tk.Button(self.sidebar , text="Home", font=fonts.large_font , background=colors.color_red , activebackground=colors.some_dark_blue , relief=tk.SUNKEN , bd=0 , foreground=colors.white_backgrond , height=1 , width=16
                                      ,activeforeground='white')
        self.settings_button  =tk.Button(self.sidebar , text="Settings", font=fonts.large_font , background=colors.color_red , activebackground=colors.some_dark_blue , relief=tk.SUNKEN , bd=0 , foreground=colors.white_backgrond , height=1 , width=16
                                      ,activeforeground='white')
        self.history_button = tk.Button(self.sidebar , text="History" , bd=0 , activebackground=colors.some_dark_blue , activeforeground=colors.white_backgrond , background=colors.color_red
                                        ,relief=tk.SUNKEN , height=1 , width=16 , font=fonts.large_font , foreground=colors.white_backgrond)
        
        ### Binding buttons for the hovering part
        self.open_close_button.bind("<Enter>" , self.open_close_hover_enter)
        self.open_close_button.bind("<Leave>" , self.open_close_hover_close)
        self.home_button.bind("<Enter>" , self.home_button_enter)
        self.home_button.bind("<Leave>" , self.home_button_leave)
        self.settings_button.bind("<Enter>" , self.settings_button_enter)
        self.settings_button.bind("<Leave>" , self.settings_button_leave)
        self.history_button.bind("<Enter>" , self.history_button_enter)
        self.history_button.bind("<Leave>" , self.history_button_leave)


    def placing_controls(self):
        self.control_frame.pack(side='top' , pady=0 , fill='x')
        self.sidebar.place(x=0 , y=24)
        self.control_button.pack(side='right' , padx=0 , pady=1)
        self.open_close_button.place(x =111 , y = 2)
        self.home_button.place(x=0,y=50)
        self.settings_button.place(x = 0 , y = 80)
        self.history_button.place(x = 0 , y=110)
        # Calling the main app
        self.dashboard.mainloop()




if __name__ == '__main__':
    hehe = Dashboard()
    hehe.defining_controls()
    hehe.placing_controls()

        
