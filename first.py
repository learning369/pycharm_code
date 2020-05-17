from tkinter import *
import math as m  #想用三角函数
root = Tk()

w = Canvas(root, width=200,height=100,background="red")
w.pack()

center_x = 100   #中心位置的x,y
center_y = 50
r = 50

#列表中存放各个点的位置
points = [
    #左上点
    center_x - int(r*m.sin(2*m.pi/5)),
    center_y -int( r*m.cos(2*m.pi/5)),
    #右上点
    center_x +int( r*m.sin(2*m.pi/5)),
    center_y -int( r*m.cos(2*m.pi/5)),
     #左下点
    center_x -int( r*m.sin(m.pi/5)),
    center_y +int( r*m.cos(m.pi/5)),
    #顶点
     center_x,
    center_y -r,
    #右下点
    center_x +int( r*m.sin(m.pi/5)),
    center_y +int( r*m.cos(m.pi/5)),
    ]
#这个就是将所有点连接起来
w.create_polygon(points,outline="green",fill="yellow")
mainloop()


