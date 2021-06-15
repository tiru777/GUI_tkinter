import time
from tkinter import *

root = Tk()
root.title("Calculator")

display = Entry(root, width=40)
display.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def button_Click(number):
   current_nu = display.get()
   display.delete(0, END)
   display.insert(0, str(current_nu) + str(number))


def button_clear():
   display.delete(0, END)


def button_add():
   first_number = display.get()
   global value
   global operator
   operator = 'add'
   value = int(first_number)
   display.delete(0, END)


def button_sub():
   first_number = display.get()
   global value
   global operator
   operator = 'Sub'
   value = int(first_number)
   display.delete(0, END)


def button_multi():
   first_number = display.get()
   global value
   global operator
   operator = 'Multi'
   value = int(first_number)
   display.delete(0, END)


def button_divi():
   first_number = display.get()
   global value
   global operator
   operator = 'divi'
   value = int(first_number)
   display.delete(0, END)


def button_equal():
   second_num = int(display.get())
   display.delete(0, END)
   if operator == 'Sub':
       display.insert(0, value - second_num)
       # time.sleep(2)
       # button_clear()
       # print('done')
   elif operator == 'add':
       display.insert(0, value + second_num)
   elif operator == 'Multi':
       display.insert(0, value * second_num)
   elif operator == 'divi':
       display.insert(0, value / second_num)


button_1 = Button(root, text='1', padx=40, pady=20, command=lambda: button_Click(1))
button_1.grid(row=1, column=0)
button_2 = Button(root, text='2', padx=40, pady=20, command=lambda: button_Click(2))
button_2.grid(row=1, column=1)
button_3 = Button(root, text='3', padx=40, pady=20, command=lambda: button_Click(3))
button_3.grid(row=1, column=2)
button_4 = Button(root, text='4', padx=40, pady=20, command=lambda: button_Click(4))
button_4.grid(row=2, column=0)
button_5 = Button(root, text='5', padx=40, pady=20, command=lambda: button_Click(5))
button_5.grid(row=2, column=1)
button_6 = Button(root, text='6', padx=40, pady=20, command=lambda: button_Click(6))
button_6.grid(row=2, column=2)
button_7 = Button(root, text='7', padx=40, pady=20, command=lambda: button_Click(7))
button_7.grid(row=3, column=0)
button_8 = Button(root, text='8', padx=40, pady=20, command=lambda: button_Click(8))
button_8.grid(row=3, column=1)
button_9 = Button(root, text='9', padx=40, pady=20, command=lambda: button_Click(9))
button_9.grid(row=3, column=2)
button_0 = Button(root, text='0', padx=40, pady=20, command=lambda: button_Click(0))
button_0.grid(row=4, column=0)
button_sum = Button(root, text='+', padx=38, pady=20, command=button_add)
button_sum.grid(row=4, column=1)
button_sub = Button(root, text='-', padx=38, pady=20, command=button_sub)
button_sub.grid(row=4, column=2)
button_mult = Button(root, text='x', padx=38, pady=20, command=button_multi)
button_mult.grid(row=5, column=0)
button_division = Button(root, text='/', padx=38, pady=20, command=button_divi)
button_division.grid(row=5, column=1)
button_clear = Button(root, text='Clear', padx=40, pady=20, command=button_clear)
button_clear.grid(row=5, column=2)
button_enter = Button(root, text='=', padx=140, pady=20, command=button_equal)
button_enter.grid(row=6, column=0, columnspan=3)

root.mainloop()

