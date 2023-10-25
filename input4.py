from tkinter import *
from config import *
from input1 import E

win = Tk()

win.geometry(size)
dari = ['' for i in range(E)]
ke = ['' for i in range(E)]
jarak = ['' for i in range(E)]
response = IntVar()
def get_jalan():
    global E
    global dari
    global ke
    global jarak
    global response
    for i in range(E):
        dari[i] = dari[i].get()
        ke[i] = ke[i].get()
        jarak[i] = jarak[i].get()
    response = response.get()
    win.destroy()

def input_jalan():
    global E
    global dari
    global ke
    global jarak
    global response
    
    Label(win, text='Masukan Rute dan Jarak').grid(row=0) 
    for i in range(E):
        dari[i] = Entry(win, width=15)
        dari[i].grid(row=i+1, column=0)
        ke[i] = Entry(win, width=15)
        ke[i].grid(row=i+1, column=1)
        jarak[i] = Entry(win, width=15)
        jarak[i].grid(row=i+1, column=2)

    Checkbutton(win, text='Kemacetan',variable=response, onvalue=1, offvalue=0).grid(row=E+1)

    Button(win, text = but_text, width = but_width, command = get_jalan).grid(row=E+2)

input_jalan()

win.mainloop()