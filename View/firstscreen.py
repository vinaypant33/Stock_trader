### Importing the pre made modules
import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import *  # To import everything and  easy to manage the code ( donthave to type tkinter.ttk etc )
from PIL import ImageTk , Image
### Importing user Made Modules
import colors
import fonts


""" Login Screen Started """
class LoginScreen():

    def __init__(self , height , width) -> None:
        self.loginscreen = tk.Tk()
        self.loginscreen.overrideredirect(True)
        self.screenheight  = self.loginscreen.winfo_screenheight()
        self.screenwidth  = self.loginscreen.winfo_screenwidth()
        self.height  =  420
        self.width  = 350 
        self.ycoordinate = (self.screenheight // 2) - (self.height //2 )
        self.xcoordinate = (self.screenwidth //2 ) - (self.width //2 )
        self.loginscreen.geometry(f"{self.width}x{self.height}+{self.xcoordinate}+{self.ycoordinate}")

    #### Defining Functions for Hover and Animation of  the  app 
    def closing_app(self):
        self.loginscreen.destroy()

    def mouse_move(self , event):
        self.x = event.x
        self.y = event.y

    def move_window(self , event):
        self.deltax = event.x - self.x
        self.deltay = event.y - self.y
        self.newx = self.loginscreen.winfo_x()  + self.deltax
        self.newy = self.loginscreen.winfo_y() + self.deltay
        self.loginscreen.geometry(f"{self.width}x{self.height}+{self.newx}+{self.newy}")
    
    def usernametextbox_enter(self , event):
        self.username_textbox.delete(0 , 'end')
        self.username_textbox.configure(foreground='black')
    
    def passwordtextbox_enter(self , event):
        self.password_textbox.delete(0 , 'end')
        self.password_textbox.configure(foreground='black')
        self.password_textbox.config(show="*")
        if self.password_textbox.focus_get == self.password_textbox:
            print("I am in focus")

    def login_button_enter(self, event):
        self.login_button.configure(background=colors.light_teal)

    def login_button_leave(self, event):
        self.login_button.configure(background=colors.sky_blue)

    def forgot_password_enter(self , event):
        self.forgot_password_label.configure(foreground=colors.some_dark_blue)
    
    def forgot_password_leave(self , event):
        self.forgot_password_label.configure(foreground=colors.light_teal)

    def register_enter(self ,  event):
        self.register_user_label.configure(foreground=colors.some_dark_blue)
    
    def register_leave(self, enter):
        self.register_user_label.configure(foreground=colors.light_teal)


    def defining_controls(self):
        #### Definign title bar and close button controls
        self.loginscreen.configure(background=colors.white_backgrond)
        self.titlebar = tk.Frame(self.loginscreen , background=colors.dark_grey , height=45 , padx=0) # Titlebar on the main login screen 
        self.titlebar.pack_propagate(1) # To make sure the Height is fixed
        self.titlebar.bind("<ButtonPress-1>", self.mouse_move) # bind control for the mouse move 
        self.titlebar.bind("<B1-Motion>" , self.move_window)
        self.close_button   = tk.Button(self.titlebar , text=" X "  , relief=tk.FLAT , bd=0 , 
        highlightthickness=0 , background=colors.dark_grey , activebackground= colors.color_red  ,
        activeforeground= colors.white_backgrond, foreground=colors.color_red , command=self.closing_app)


        #### Defining the user related controls for the login Code

        """ Label for the Login Screen """
        self.login_label  = tk.Label(self.loginscreen , text="LOGIN" , font=fonts.super_large_font , foreground=colors.light_teal , background=colors.white_backgrond )

        # Definign Image for the Login Screen  : 
        self.avater_image  = Image.open(r"View\assets\avatar-2.png")
        self.resized_avater_image = self.avater_image.resize((150 , 150))
        self.login_avatar_image  = ImageTk.PhotoImage(self.resized_avater_image)
        self.avatar_label  = tk.Label(self.loginscreen , image=self.login_avatar_image)



        self.username_textbox  = tk.Entry(self.loginscreen  , font = fonts.large_font , foreground='grey' , width=36 , border=0)
        self.username_textbox.insert(0 , " Enter Username " )
        # self.username_textbox.bind("<Enter>" , self.usernametextbox_enter)
        self.username_textbox.bind("<ButtonPress-1>" , self.usernametextbox_enter)
        
        self.username_bottom_border  = tk.Frame(self.loginscreen , height=2 , width = 330 , background=colors.dark_grey)

        self.password_textbox  = tk.Entry(self.loginscreen , font=fonts.large_font , foreground='grey' , width=36 , border=0 )
        self.password_textbox.insert( 0 , " Enter Password ")
        self.password_textbox.bind("<ButtonPress-1>" , self.passwordtextbox_enter)
        
        self.password_bottm_border  = tk.Frame(self.loginscreen , height=2 , width=330 , background=colors.dark_grey)

        self.login_button = tk.Button(self.loginscreen , text="Login" , font=fonts.medium_font , height=2, width=40 , bd=0 , activebackground=colors.some_dark_blue, 
                                      relief=tk.FLAT , foreground=colors.dark_blue , background=colors.sky_blue)


        self.login_button.bind("<Enter>" , self.login_button_enter)
        self.login_button.bind("<Leave>" , self.login_button_leave)


        ### Forgot and Register Username controls
        self.forgot_password_label  = tk.Label(self.loginscreen ,text="Forgot Password !!" , background=colors.white_backgrond ,  foreground=colors.light_teal ,font=fonts.medium_font)
        self.register_user_label  = tk.Label(self.loginscreen ,text="Register User !!" , background=colors.white_backgrond ,  foreground=colors.light_teal ,font=fonts.medium_font)

        self.forgot_password_label.bind("<Enter>" , self.forgot_password_enter)
        self.forgot_password_label.bind("<Leave>" , self.forgot_password_leave)

        self.register_user_label.bind("<Enter>" , self.register_enter)
        self.register_user_label.bind("<Leave>" , self.register_leave)


    def placing_controls(self):
        ## Placing the titlebar and the closing button 
        self.titlebar.pack(side='top'  , fill='x')
        self.close_button.pack(side='right' , padx=5)

        # As the app interface would be the same will be using he place rather than pack
        self.login_label.place(x=130 , y=20)
        self.avatar_label.place(x = 100 , y=75)
        self.username_textbox.place(x=10 , y=250)
        self.username_bottom_border.place(x = 10 , y = 270)

        self.password_textbox.place(x = 10 , y = 290)
        self.password_bottm_border.place(x = 10 , y = 310)
        self.login_button.place(x=12 , y=330)

        self.forgot_password_label.place(x=10 , y = 380)
        self.register_user_label.place(x = 240 , y=380)

       
        # Calling the main app  
        self.loginscreen.mainloop()

    def closing_app(self):
        self.loginscreen.destroy()


""" Login Screen Ended """



""" Register Screen Started """
""" Username button Password Button Secret Question ( to chose from the user ) 
and secret answer have to be in the form of text 
"""

class Registerscreen():

    def __init__(self) -> None:
        pass




""" Register Screen Ended """

if __name__ == '__main__':
    lsc = LoginScreen(420 , 350)
    lsc.defining_controls()
    lsc.placing_controls()
    