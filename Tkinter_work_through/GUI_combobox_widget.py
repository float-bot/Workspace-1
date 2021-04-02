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
action.grid(column=2, row=1)
#action.config(state='disabled')

'''Basic Label, "A label"'''
a_label = ttk.Label(win, text='A Label')
a_label.grid(column=0, row=0)

'''name entry text box'''
name = tk.StringVar()
name_entered = ttk.Entry(win, width=12, textvariable=name)
name_entered.grid(column=0, row=1)
name_entered.focus()

ttk.Label(win, text='Choose a number:').grid(column=1,row=0)

number = tk.StringVar()
number_chosen = ttk.Combobox(win, width=12, textvariable=number)
number_chosen['value']=(1,2,4,42,100)
number_chosen.grid(column=1,row=1)
number_chosen.current(0)


'''GUI Start point'''
win.mainloop()