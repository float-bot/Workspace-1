'''=====================
        IMPORTS
   ====================='''


import tkinter as tk
from tkinter import Grid, ttk
from tkinter.constants import DISABLED
from typing import Text

'''======================
        Definitions
   ======================'''

def click_me():
    action.config(text='Hello '+ name.get())
    action.config(state='disabled')

'''Calling tk'''
win = tk.Tk()

'''Window Title'''
win.title('Python GUI')

'''Basic Button'''
action = ttk.Button(win, text = 'Click Me!', command=click_me)
action.grid(column=1, row=1)
#action.config(state='disabled')

'''Basic Label'''
a_label = ttk.Label(win, text='A Label')
a_label.grid(column=0, row=0)

'''Name entry text box'''
name = tk.StringVar()
name_entered = ttk.Entry(win, width=12, textvariable=name)
name_entered.grid(column=0, row=1)
name_entered.focus()

'''GUI Start point'''
win.mainloop()