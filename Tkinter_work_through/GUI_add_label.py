#===========================
#IMPORTS
#===========================

import tkinter as tk
from tkinter import Grid, ttk

win = tk.Tk()

win.title('Python GUI')

ttk.Label(win, text='A Label').grid(column=0, row=0)

#win.resizable(False,False)

win.mainloop()