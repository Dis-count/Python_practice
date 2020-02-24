import turtle

turtle.bgcolor('black')
turtle.color('yellow')

#编写一个函数drawShape，用于画多边形
def drawShape(totalTimes,distance):
    for time in range(totalTimes):
        turtle.forward(distance)
        turtle.left(360/totalTimes)

#调用这个函数，来画一个五边形，每边长度为80个像素
drawShape(6,100)
