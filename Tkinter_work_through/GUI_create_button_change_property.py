#===========================
#IMPORTS
#===========================

import tkinter as tk
from tkinter import Grid, ttk
from typing import Text

def click_me():
    action.configure(text = '** I have been clicked **')
    a_label.configure(foreground = 'red')
    a_label.configure(text = 'A red label')



win = tk.Tk()

win.title('Python GUI')

action = ttk.Button(win, text = 'Click Me!', command=click_me)
action.grid(column=1, row=0)

a_label = ttk.Label(win, text='A Label')
a_label.grid(column=0, row=0)
#win.resizable(False,False)

win.mainloop()