import turtle
turtle.bgcolor('black')
turtle.color('yellow')

#先画后轮子
turtle.fillcolor("yellow")
turtle.begin_fill()
turtle.circle(20)
turtle.end_fill()
#提笔往前挪，画前轮
turtle.penup()
turtle.forward(200)
turtle.pendown()
turtle.begin_fill()
turtle.circle(20)
turtle.end_fill()
#画车轮廓
turtle.left(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(70)
turtle.left(135)
turtle.forward(60)
turtle.right(45)
turtle.forward(2)
turtle.left(90)
turtle.forward(70)
turtle.right(90)
turtle.forward(20)
turtle.left(90)
turtle.forward(160)
turtle.left(50)
turtle.forward(60)
turtle.left(40)
turtle.forward(18)
turtle.left(90)
turtle.forward(240)
#画后轮与车轮廓接触线
turtle.penup()
turtle.home()
turtle.pendown()
turtle.left(90)
turtle.forward(50)
turtle.write("This car is made by Discount,2020")

#车上方写标题
turtle.penup()
turtle.setpos(60,140)
turtle.pendown()
turtle.write("别问！",font=("Times", 18, "bold"))

#隐藏那个画笔箭头
turtle.hideturtle()

import time
time.sleep(5)
