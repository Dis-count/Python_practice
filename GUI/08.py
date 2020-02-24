import turtle
turtle.bgcolor('black')
turtle.color('yellow')

#先画笑脸轮廓,画一个半径为100像素的圆
turtle.fillcolor("yellow")
turtle.begin_fill()
turtle.circle(100)
turtle.end_fill()

#提笔到左上角（-40，120）位置，画一个小圆，表示右眼
turtle.pen(pensize=10,pencolor='red',fillcolor='yellow')
turtle.penup()
turtle.setpos(-40,120)
turtle.pendown()
turtle.circle(10)

#提笔到中部位置，先画一条短线表示上嘴唇
turtle.penup()
turtle.setpos(-10,60)
turtle.pendown()
turtle.forward(20)
#继续下移一定距离，画一条短弧线表示下嘴唇
turtle.penup()
turtle.setpos(-10,40)
turtle.pendown()
totalTimes=4
for times in range(totalTimes):
    turtle.forward(5)
    turtle.left(10)

#提笔到右上角（40，120）位置，画一个小圆，表示右眼
turtle.pen(pensize=10,pencolor='red',fillcolor='yellow')
turtle.penup()
turtle.setpos(40,120)
turtle.pendown()
turtle.circle(10)
#隐藏那个画笔箭头
turtle.hideturtle()
