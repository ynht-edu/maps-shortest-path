from tkinter import *
from config import *

win = Tk()

win.geometry(size)

def get_jumlah():
   global Start_input
   global End_input
   global V_avg
   Start_input = Start_input.get()
   End_input = End_input.get()
   V_avg = int(V_avg.get())
   win.destroy()

def input_jumlah():
   global Start_input
   global End_input
   global V_avg
   Label(win, text='Dimulai Dari').grid(row=0) 
   Label(win, text='Tujuan').grid(row=1)
   Label(win, text='Kelajuan Rata-Rata(km/j)').grid(row=2) 

   Start_input = Entry(win)
   End_input = Entry(win)
   V_avg = Entry(win)
   Start_input.focus_set()
   Start_input.grid(row=0, column=1)
   End_input.grid(row=1, column=1)
   V_avg.grid(row=2, column=1)


   Button(win, text = but_text, width = but_width, command = get_jumlah).grid(row=3)

input_jumlah()
win.mainloop()