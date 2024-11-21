from tkinter import *

master_window = Tk()

# Menu
menu1 = Menu(master_window)
master_window.config(menu=menu1)
filemenu = Menu(menu1)
menu1.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New")

master_window.mainloop()

