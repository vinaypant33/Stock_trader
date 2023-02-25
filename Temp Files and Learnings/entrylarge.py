from tkinter import *
obj = Tk()

obj.geometry('200x200')


def click(*args):
  placeholder.delete(0, 'end')


def leave(*args):
  placeholder.delete(0, 'end')
  placeholder.insert(0, 'I am placeholder')
  obj.focus()



placeholder = Entry(obj, width=60)


placeholder.insert(0, 'Enter Text:- ')
placeholder.pack(pady=10)


placeholder.bind("<Button-1>", click)
placeholder.bind("<Leave>", leave)


obj.mainloop()