#===========================
#IMPORTS
#===========================

import tkinter as tk
from tkinter import Grid, ttk
from typing import Text

def click_me():
    action.configure(text='Hello '+ name.get())



win = tk.Tk()

win.title('Python GUI')

action = ttk.Button(win, text = 'Click Me!', command=click_me)
action.grid(column=1, row=0)

a_label = ttk.Label(win, text='A Label')
a_label.grid(column=0, row=0)

name = tk.StringVar()
name_entered = ttk.Entry(win, width=12, textvariable=name)
name_entered.grid(column=0, row=1)
#win.resizable(False,False)

win.mainloop()