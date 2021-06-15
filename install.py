from tkinter import *

main_window = Tk()

Label(main_window, text="Select Path").grid(row=5, column=0)
e = Entry(main_window, width=25)
e.grid(row=5, column=1)


def click():
   v = e.get()
   print(v)
   Label(main_window, text="hello" + v).grid(row=11, column=0)


Button(main_window, text="Back", width=20).grid(row=10, column=3)
Button(main_window, text="Next", width=20, command=click).grid(row=10, column=4)
Button(main_window, text="Cancel", width=20).grid(row=10, column=5)

main_window.mainloop()
