from tkinter import *

if __name__ == '__main__':
    canvas = Canvas(width=700, height=700, bg='white')
    canvas.pack(expand=YES, fill=BOTH)
    x0 = 300
    y0 = 300
    y1 = 400
    x1 = 400
    for i in range(5):
        canvas.create_line(x0,y0,x0,y1, width=5, fill='blue')
        x0 = x0 -20
        y0 = y0 - 20
        x1 = x1 + 20
        y1 = y1 + 20
        x0 = 330
        y1 = 375
        y0 = 300
    for i in range(5):
        canvas.create_line(x0,y0,x0,y1,width=5,fill = 'green')
        x0 += 20
        y0 += 20
        y1 += 20
    mainloop()
