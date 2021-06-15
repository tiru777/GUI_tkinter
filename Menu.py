from tkinter import *
import tkinter as tk
main_window =tk.Tk()
menu = Menu(main_window)
main_window.config(menu=menu)

filemenu = Menu(menu)
menu.add_cascade(label='File',menu=filemenu)
filemenu.add_command(label='New')
filemenu.add_command(label='Save')
filemenu.add_command(label='Save As')

menu.add_cascade(label='About')
menu.add_cascade(label='Help')
main_window.mainloop()
