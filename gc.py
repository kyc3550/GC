import matplotlib.pyplot as plt
from tkinter import *
import numpy as np
def DDALine(x1, y1, x2, y2, color):
        dx = int(x2) - int(x1)
        dy = int(y2) - int(y1)
        steps = 0
        if abs(dx) > abs(dy):
            steps = abs(dx)
        else:
            steps = abs(dy)
        delta_x = float(dx / steps)
        delta_y = float(dy / steps)
        x = int(x1) + 0.5
        y = int(y1) + 0.5
        for i in range(0, int(steps + 1)):
            plt.plot(int(x), int(y), color)
            x += delta_x
            y += delta_y
        plt.show()
        
def line():
    line = Tk()
    line.title("선그리기")
    line.geometry("250x150")

    infos=["x1","y1","x2","y2"]
    a=0
    for c in infos:
        Label(line,text=c,width='8').grid(row=a,column=0)
        a=a+1

    a=Entry(line,width=10)
    a.grid(row=0,column=1)
      
    b=Entry(line,width=10)
    b.grid(row=1,column=1)

    
    c=Entry(line,width=10)
    c.grid(row=2,column=1)

    
    d=Entry(line,width=10)
    d.grid(row=3,column=1)
    
    Button(line,text="DDA",width='10',command=lambda : DDALine(a.get(), b.get(), c.get(), d.get(), 'r.')).grid(row=1,column=2)


main = Tk()
main.title("CG 중간대체 과제")
main.geometry("200x150")

Button(main,text="선 그리기",width='20', command = line).pack()

main.mainloop()
