from tkinter import *
from config import *
win = Tk()

win.geometry(size)

def get_jumlah():
   global n_kota
   global n_jalan
   global N
   global E
   N = int(n_kota.get())
   E = int(n_jalan.get())
   win.destroy()

def input_jumlah():
   global n_kota
   global n_jalan
   Label(win, text='Jumlah Kota').grid(row=0) 
   Label(win, text='Jumlah Jalan').grid(row=1) 

   n_kota = Entry(win)
   n_jalan = Entry(win)
   n_kota.focus_set()
   n_kota.grid(row=0, column=1)
   n_jalan.grid(row=1, column=1)


   Button(win, text = but_text, width = but_width, command = get_jumlah).grid(row=2)

input_jumlah()
win.mainloop()