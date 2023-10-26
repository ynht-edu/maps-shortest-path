from tkinter import *
from config import *
from input1 import N

win = Tk()

win.geometry(size)
index = {}
def get_kota():
    global N
    global index
    global node

    for i in range(1, N+1):
        index[i] = index[i].get()
        node = index[i]
        index[node] = i
    win.destroy()

def input_kota():
    global N
    global index
    global node
    
    Label(win, text='Masukan Kota').grid(row=0) 
    for i in range(1, N+1):
        index[i] = Entry(win)
        index[i].grid(row=i)
        win.update()

    Button(win, text = but_text, width = but_width, command = get_kota).grid(row=N+1)

input_kota()

win.mainloop()