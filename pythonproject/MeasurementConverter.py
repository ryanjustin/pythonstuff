from Tkinter import *
import time as tm

def time():
    L1.configure(text = "seconds")
    L2.configure(text = "minutes")
    L3.configure(text = "hours")
    L4.configure(text = "days")
    top.update()
def Weight():
    L1.configure(text = "oz")
    L2.configure(text = "lbs")
    L3.configure(text = "tons")
    top.update()
def Distance():
    L1.configure(text = "inches")
    L2.configure(text = "feet")
    L3.configure(text = "yards")
    L4.configure(text = "miles")
    top.update()





def convert(measure1):
    pass






top = Tk()

top.geometry("700x400")

B0 = Button(top, height = 2, width = 12, text = "", font =("purisa", 10), command = lambda : time())
B1 = Button(top, height = 2, width = 12, text = "Time", font =("purisa", 10), command = lambda : time())
B2 = Button(top, height = 2, width = 12, text = "Weight", font =("purisa", 10), command = lambda : Weight())
B3 = Button(top, height = 2, width = 12, text = "Distance", font =("purisa", 10), command = lambda : Distance())
B4 = Button(top, height = 2, width = 12, text = "", font =("purisa", 10), command = lambda : Distance())
B5 = Button(top, height = 2, width = 5, text = "Convert", font =("purisa", 10), command = lambda : convert())
L1 = Label(top, height = 1, width = 5, text = "",font = ("purisa", 20),bd = 1)
L2 = Label(top, height = 1, width = 5, text = "",font = ("purisa", 20),bd = 1)
L3 = Label(top, height = 1, width = 5, text = "",font = ("purisa", 20),bd = 1)

B0.grid(column = 0, row = 1, padx = 5)
B1.grid(column = 1, row = 1, padx = 5)
B2.grid(column = 2, row = 1, padx = 5)
B3.grid(column = 3, row = 1, padx = 5)
B4.grid(column = 4, row = 1, padx = 5)
L1.grid(column = 2, row = 3, pady = 5)
L2.grid(column = 2, row = 4, pady = 5)
L3.grid(column = 2, row = 5, pady = 5)
B5.grid(column = 2, row = 7,pady = 12, padx = 12)




top.mainloop()
