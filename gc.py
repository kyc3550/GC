import numpy as np
import matplotlib.patches as patches
from tkinter import *
from functools import partial
import matplotlib.pyplot as plt
import math


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
        
def bresenham(x1,y1,x2,y2,color):
	dx = int(x2)-int(x1)
	dy = int(y2)-int(y1)

	D = 2*dy - dx
	
	y = int(y1)

	for x in range(int(x1)+1,int(x2)+1):
		if D > 0:
			y += 1
			plt.plot(x,y,color)
			D += (2*dy-2*dx)
		else:
			plt.plot(x,y,color)
			D += 2*dy
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
    Button(line,text="Bresenham",width='10',command=lambda : bresenham(a.get(), b.get(), c.get(), d.get(), 'r.')).grid(row=2,column=2)
    
def Dtri(x1,y1,x2,y2,x3,y3,tri):
        def Scale(x1,y1,x2,y2,x3,y3,s1,s2):
                point1 = [int(x1),int(x2),int(x3)]
                point2 = [int(y1),int(y2),int(y3)]
                sp1=[]
                sp2=[]
                nsp=[]
                a=0
                for x in point1:
                        sp1.append(x * int(s1))
                
                for y in point2:
                        sp2.append(y * int(s2))
               
                while a<3:
                    nsp.append([sp1[a],sp2[a]])
                    a=a+1

               
                
                X=np.array([-300,300])
                Y=np.array([-300,300])

                plt.plot(X,Y,color='None')

                point=np.array([nsp[0],nsp[1],nsp[2]])

                tri=patches.Polygon(point, fill=None ,edgecolor='k',ls='solid',lw=1)

                plt.gca().add_patch(tri) 
                plt.show()
                
        def rotate(x1,y1,x2,y2,x3,y3,n,a):
                rot = np.array([[math.cos(a),math.sin(-a)],[math.sin(a),math.cos(a)]])
                if n==1:
                    v2 = np.array([[int(x2)],[int(y2)]])
                    v3 = np.array([[int(x3)],[int(y3)]])
                    rot_v2 = np.dot(rot,v2)
                    rot_v3 = np.dot(rot,v3)
                   
                    X=np.array([-300,300])
                    Y=np.array([-300,300])
                    plt.plot(X,Y,color='None')
                    rot_point=np.array([[x1,y1],[rot_v2[0][0],rot_v2[1][0]],[rot_v3[0][0],rot_v3[1][0]]])
                    rot_tri=patches.Polygon(rot_point, fill=None ,edgecolor='k',ls='solid',lw=1)
                    plt.gca().add_patch(rot_tri)
                    plt.show()

        rot_v=Entry(tri,width=10)
        rot_v.grid(row=5,column=1)
        Label(tri,text="회전",width='8').grid(row=0,column=3)           

        n=IntVar()
        radio1=Radiobutton(tri, text = "1",value=1, variable=n, command = lambda : rotate(x1,y1,x2,y2,x3,y3,1,int(rot_v.get()))).grid(row=1, column=3)
        radio2=Radiobutton(tri, text = "2",value=2, variable=n, command = lambda : rotate(x1,y1,x2,y2,x3,y3,2,int(rot_v.get()))).grid(row=2, column=3)
        radio3=Radiobutton(tri, text = "3",value=3, variable=n, command = lambda : rotate(x1,y1,x2,y2,x3,y3,3,int(rot_v.get()))).grid(row=3, column=3)

   
        Button(tri,text="신축",width='10', command=lambda : Scale(x1,y1,x2,y2,x3,y3,int(s1.get()),int(s2.get()))).grid(row=6,column=2)

        s1=Entry(tri,width=10)
        s1.grid(row=4,column=1)
        s2=Entry(tri,width=10)
        s2.grid(row=4,column=2)
        
        plt.plot(X,Y)

        point=np.array([[x1,y1],[x2,y2],[x3,y3]])
        tri=patches.Polygon(point, fill=None ,edgecolor='k',ls='solid',lw=1)

        plt.gca().add_patch(tri)

        plt.show()

        
def tri():
    tri = Tk()
    tri.title("삼각형 그리기")
    tri.geometry("310x180")
    Label(tri,text="x",width='8').grid(row=0,column=1)
    Label(tri,text="y",width='8').grid(row=0,column=2)

    infos=["좌표1","좌표2","좌표3","배율","회전각"]
    a=1
    for c in infos:
        Label(tri,text=c,width='8').grid(row=a,column=0)
        a=a+1

    x1=Entry(tri,width=10)
    x1.grid(row=1,column=1)      
    y1=Entry(tri,width=10)
    y1.grid(row=1,column=2)


    x2=Entry(tri,width=10)
    x2.grid(row=2,column=1)   
    y2=Entry(tri,width=10)
    y2.grid(row=2,column=2)
    
    x3=Entry(tri,width=10)
    x3.grid(row=3,column=1)   
    y3=Entry(tri,width=10)
    y3.grid(row=3,column=2)

    Button(tri,text="그리기",width='10',command=lambda : Dtri(x1.get(),y1.get(),x2.get(),y2.get(),x3.get(),y3.get(),tri)).grid(row=6,column=1)

def Dcir(x,y,redius):

        center = (int(x),int(y))
        redius_ = int(redius)
        draw_circle = plt.Circle(center, redius_, fill=False)

        a = plt.axes(xlim=(-100,100),ylim=(-100,100))
        a.add_patch(draw_circle)
        a.set_aspect('equal')

        plt.title('Circle')
        plt.show()
        
def circle():
        cir = Tk()
        cir.title("원 그리기")
        cir.geometry("250x100")
        
        Label(cir,text="x",width='8').grid(row=0,column=1)
        Label(cir,text="y",width='8').grid(row=0,column=2)

        infos=["좌표","반지름"]
        a=1
        for c in infos:
                Label(cir,text=c,width='8').grid(row=a,column=0)
                a=a+1

        x=Entry(cir,width=10)
        x.grid(row=1,column=1)      
        y=Entry(cir,width=10)
        y.grid(row=1,column=2)

        redius=Entry(cir,width=10)
        redius.grid(row=2,column=1)

        Button(cir,text="그리기",width='10',command=lambda : Dcir(x.get(),y.get(),redius.get())).grid(row=2,column=2)
        


main = Tk()
main.title("CG 중간대체 과제")
main.geometry("200x150")

Button(main,text="선 그리기",width='20', command = line).pack()
Button(main,text="삼각형 그리기",width='20', command=tri).pack()
Button(main,text="원 그리기",width='20', command= circle).pack()


main.mainloop()
