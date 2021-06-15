import tkinter as tk
from tkinter import *

main_window = tk.Tk()
main_window.title(" Sadguruvenamha ")

# widgets
"""
button To add a button in your application
button(master, text='',width=20,height=40,command = function)
"""
button = tk.Button(main_window, text='guru', width=25, height=20, bg="#457890", command=main_window.destroy)
# button.pack()
# button.grid()
# button.place()

#
"""
canvas =  It is used to draw pictures and other complex layout like graphics, text and widget
canvas(master,width=value,height=value,bg=color,bd=color,cursor=value)
"""
canvas = tk.Canvas(main_window, width=20, height=50)
canvas_width = 20
canvas.create_line(0, 10, canvas_width, 10)
# canvas.pack()

"""
checkButton = to select any number of option
checkButton  = CheckButton(master,bg=value,command=function,Title="text")
"""
var1 = tk.IntVar()
checkButton_Ma = tk.Checkbutton(main_window, variable=var1, text="Male")
# print(var1)
checkButton_Fe = tk.Checkbutton(main_window, text="Female")
# checkButton_Ma.grid(row=0, column=1)
# checkButton_Fe.grid(row=1, column=1)


"""
Entry:It is used to input the single line text entry from the user
entry = tk.Entry (main_window,bd=color,bg=color,height=value,width=value,command=value)
"""

first_name = tk.Label(main_window, text="First Name").grid(row=0, column=0)
last_name = tk.Label(main_window, text='Last Name').grid(row=1, column=0)

first_name_entry = Entry(main_window)
first_name_entry .grid(row=0, column=1)

second_name_entry = Entry(main_window)
second_name_entry.grid(row=1, column=1)
# radiobutton
v = tk.IntVar()
tk.Radiobutton(main_window, text="Male", variable=v, value=1).grid(row=3, column=0)
tk.Radiobutton(main_window, text="Female", variable=v, value=2).grid(row=4, column=0)

# Text
Label(main_window, text="Address").grid(row=5, column=0)
text = Text(main_window, height=2, width=20).grid(row=5, column=1)
# text.insert(END,"Achala sadguru \n sri penchulayarya\nswamy")
# check button
tk.Checkbutton(main_window, text="Terms and Conditions").grid(row=7, column=1)


# button
def click():
   data_f = first_name_entry.get()
   data_s = second_name_entry.get()
   print(data_f, data_s)
   Label(main_window, text="hello" + data_f).grid(row=10,column=0)
   Label(main_window, text="hello" + data_s).grid(row=11,column=0)
   # Label(main_window, text="hello tiru" ).grid(row=10,column=0)


# tk.Button(main_window, text="Submit", width=20, command=main_window.destroy).grid(row=8, column=1)
Button(main_window, text="Submit", width=20, command=click).grid(row=8, column=1)

Label(main_window, text='Drop Down').grid(row=9, column=0)
l = Listbox(main_window)
l.insert(1, 'Sadguru')
l.insert(2, 'nana')
l.insert(3, 'ayya')
l.grid(row=9, column=1)

# message


# To run the main window infinite times
main_window.mainloop()

# some of methods are there to split the main window
# pack() is used to split blocks by block main window
# grid() is used to table like structure of main window
# place() is used directly put widget in particular to place
# command is used to call the f unction
