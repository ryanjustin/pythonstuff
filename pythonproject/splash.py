from Tkinter import *
import subprocess








top = Tk()

top.geometry("700x800")
B1 = Button(top, text = "simple calculator",height = 10,width = 12, command = lambda : subprocess.call("python simpleCalc.py", shell = True))

B1.grid(column = 0, row = 0, padx = 10, pady =10)






top.mainloop()


