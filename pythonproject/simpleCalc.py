
from Tkinter import *




def changeSign(v3):
    if (v3 == "+"):
        B2.config(text = "X")
        B1.config(command = lambda : multiply(E1.get(),E2.get()))
    if (v3 == 'X'):
        B2.config(text = "/")
        B1.config(command = lambda : divide(E1.get(),E2.get()))
    if (v3 == '/'):
        B2.config(text = "-")
        B1.config(command = lambda : subtract(E1.get(),E2.get()))
    if (v3 == '-'):
        B2.config(text = "+")
        B1.config(command = lambda : add(E1.get(),E2.get()))
    B2.text = v3

def add(value1, value2):
    result.config(font = ("purisa", 24))
    if (value1.isdigit() and value2.isdigit()):
        value3 = int(value2) + int(value1)
        result.config(text = value3)
    else:
        print "thats not a number!"
        result.config(text = "thats not a number!",font = ("purisa", 10))
                      

def multiply(value1, value2):
    result.config(font = ("purisa", 24))
    if (value1.isdigit() and value2.isdigit()):
        value3 = int(value1)*int(value2)
        result.config(text = value3)
    else:
        print "thats not a number!"
        result.config(text = "thats not a number!",font = ("purisa", 10))

def divide(value1, value2):
    result.config(font = ("purisa", 24))
    if (value1.isdigit() and value2.isdigit()):
        value3 = int(value1)/int(value2)
        result.config(text = value3)
    else:
        print "thats not a number!"
        result.config(text = "thats not a number!",font = ("purisa", 10))

def subtract(value1, value2):
    result.config(font = ("purisa", 24))
    if (value1.isdigit() and value2.isdigit()):
        value3 = int(value1)-int(value2)
        result.config(text = value3)
    else:
        print "thats not a number!"
        result.config(text = "thats not a number!",font = ("purisa", 10))
        
    


#v3 = "+"
top = Tk()
top.geometry("550x250")
E1 = Entry(top, bd = 1, bg = "light grey")
E2 = Entry(top, bd = 1, bg = "light grey")
B1 = Button(top,text = "CALCULATE!",height = 1, width = 10,command = lambda : add(E1.get(),E2.get()),font = ("purisa",16),bd = 0)
B2 = Button(top, text = '+', height = 1, width = 10, command = lambda : changeSign(B2["text"]),font = ("purisa",16),bd = 0)



E1.grid(padx = 15,column = 1, row = 0, pady = 20)


E2.grid(padx = 15, column = 4, row = 0, pady = 20)
B2.grid(column = 2, row = 0,pady =10)
B1.grid(column = 2, rowspan = 20, pady = 10)
result = Label(top, bd =5, text = "0", font = ("purisa",24))

result.grid(column = 2, pady = 30)



top.mainloop()





