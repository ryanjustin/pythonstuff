
from Tkinter import *


def changeSign(v3):
    print v3
    if (v3 == "+"):
        B2.config(text = "X")
    if (v3 == 'X'):
        B2.config(text = "/")
    if (v3 == '/'):
        B2.config(text = "-")
    if (v3 == '-'):
        B2.config(text = "+")
    B2.text = v3
    print B2.text

def add(value1, value2):
    value3 = value2 + value1
    print value3
    print "adding!"
    exit
    return value3

v3 = "+"
top = Tk()
top.geometry("575x300")
L1 = Label(top, text="Value 1: ")
E1 = Entry(top, bd =5)
L2 = Label(top,text="Value 2:")
E2 = Entry(top, bd = 5)
value1 = E1.get()
value2 =E2.get()
B1 = Button(top,text = "calculate",height = 1, width = 10,command = lambda : add(value1,value2))
B2 = Button(top, text = v3, height = 1, width = 10, command = lambda : changeSign(B2.text))

L1.grid(column = 0, row = 0)
E1.grid(column = 1, row = 0)

L2.grid(column = 3, row = 0)
E2.grid(column = 4, row = 0)
B2.grid(column = 2, row = 0)
B1.grid(column = 2, rowspan = 20)


top.mainloop()





