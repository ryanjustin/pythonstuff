from Tkinter import *
import time as tm



def start(H,M,S):
    if(running):
        pass
    elif(stopped):
        global running
        running = True
        run(H,M,S)

def stop():
    global stopped
    stopped = True
    global running
    running = False
    now = tm.time()
    if(running):
        quit()
    elif(stopped):
        reset()

def run(H,M,S):
    global running
    running = True
    
    print "{}{}{}".format(H,M,S)
    L1.config(text = "{}:{}:{}".format(H,M,S))

    global stopped
    stopped = False
    now = tm.time()
    S = tm.time() - now
    if(S == 60):
        S = 0
        M = M+1
    if(M == 60):
        M = 0
        H = H +1
        
def reset():
    pass






top = Tk()
top.geometry("350x200")



global H
H = 0
global M
M = 0
global S
S = 0
running  = False
stopped = True



B1 = Button(top, height = 5, width = 10, text = "START", font =("purisa", 10), command = lambda : start(H,M,S))
L1 = Label(top, height = 1, width = 5, text = "{}:{}:{}".format(H,M,S),font = ("purisa", 24),bd = 1)   
B2 = Button(top, height = 5, width = 10, text = "STOP/RESET", font = ("purisa", 10), command = lambda : stop())



L1.grid(column = 1, row = 0)
B1.grid(column = 0, row = 2, padx = 12)
B2.grid(column = 3, row = 2)

print running
while(running):
    run(H,M,S)
    


top.mainloop()










