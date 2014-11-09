from Tkinter import *
import time as tm

def start():
    global M,H,S
    global running
    if(running):
        pass
    else:
        running = True
        global stopped
        stopped = False

        while(running == True):
            top.update()
            N = tm.time()
            tm.sleep(.1)
            S = float (S) + (float (format(tm.time(), '.2f')) - N)
            if(S > 60):
                S = 0
                M = M+1
            if(M > 60):
                M = 0
                H = H+1

            L1.config(text = "{} :".format(format(H, '.0f')))
            L2.config(text = "{} :".format(format(M, '.0f')))
            L3.config(text = "{}".format(format(S,'.2f')))
            if(stopped == True):
                break

def stop():
    global running,stopped,S,M,H
    if(stopped == True):
        S = 0
        M = 0
        H = 0
        L1.config(text = "{} :".format(0))
        L2.config(text = "{} :".format(0))
        L3.config(text = "{}".format(0))
        top.update()

    if(stopped == False):
        running = False
        stopped = True

    #main(running,stopped)



top = Tk()
global running
running = False
global stopped
stopped = True
global H
global M
global S
H = 0
M = 0
S = 0

top.geometry("580x200")


B1 = Button(top, height = 5, width = 10, text = "START", font =("purisa", 10), command = lambda : start())
L1 = Label(top, height = 1, width = 5, text = "{} :".format(H),font = ("purisa", 28),bd = 1)
L2 = Label(top, height = 1, width = 5, text = "{} :".format(M),font = ("purisa", 28),bd = 1)
L3 = Label(top, height = 1, width = 5, text = "{}".format(S),font = ("purisa", 28),bd = 1)
B2 = Button(top, height = 5, width = 10, text = "STOP/RESET", font = ("purisa", 10), command = lambda : stop())


L1.grid(column = 1, row = 1)
L2.grid(column = 2, row = 1)
L3.grid(column = 3, row = 1)
B1.grid(column = 0, row = 2, padx = 12)
B2.grid(column = 4, row = 2)



top.mainloop()
