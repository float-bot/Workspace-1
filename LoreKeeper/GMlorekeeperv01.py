'''writen by john glueck, johnglueck1s@gmail.com
This is opensource, do what you want, I don't care.'''

import tkinter as tk
from tkinter import Button, Frame, Grid, ttk
from tkinter.constants import BOTTOM, FALSE, LEFT, RIGHT

def frame_initiative(x):
    '''===================================================================================
        The frame for the initiative options is contained here. 
        need to add a section that automates the turn progression and gives stat readouts. 
        That might need to be in a seperate frame off to the right though.
        Adding it here might make this definition too big.
        =================================================================================='''
    global frame_initiative_open
    if frame_initiative_open == False:
        print('DEBUG: frame initiative displayed') #Debug, delete this at some point.==================================
        frame_initiative = Frame(window_main)
        frame_initiative.pack(side=LEFT)
        button_add_npc = Button(frame_initiative, activebackground='#909090', text="Add NPC", activeforeground='#990099', bd=10, width=25, command=add_npc)
        button_close = Button(frame_initiative, activebackground='#909090', text="close", activeforeground='#990099', bd=10, width=25, command=frame_initiative.destroy())
        button_add_npc.pack()
        button_close.pack()
        frame_initiative_open = True
def add_npc():
    global add_npc_open
    if add_npc_open == False:
        print('DEBUG: add npc window displayed') #Debug, delete this at some point===============================================
        window_add_npc = tk.Tk()
        window_add_npc.title('Add NPC Info')
        window_add_npc.geometry('500x500')
        window_add_npc.resizable(False,False)
        window_add_npc['background']='#aaaa00'
        add_npc_open = True 

frame_initiative_open = False
add_npc_open = False

window_main = tk.Tk()
window_main.title("Lore Keeper v0.1")
window_main.geometry("1500x1000")
window_main.resizable(False,False)
window_main['background']='#aaaa00' #Gray Background in the main window

button_initiative = Button(window_main, activebackground='#909090', text="Initiative", activeforeground="#990099", bd=10, width=25, command=lambda:frame_initiative(frame_initiative_open))
button_initiative.pack(side=LEFT)

window_main.mainloop()