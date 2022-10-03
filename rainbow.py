import turtle  #to draw using pen

draw = turtle.Turtle()
speed = 0
t1 = 0
for k in range(1, 180 + 1, 1):  #the main loop to rotate the complete rainbow

    if k < 145:
        t1 = (t1 + k * 0.3) % 360  #constantly speeding up
    else:
        if k < 180:
            t1 = (t1 + k * 0.05) % 360  #stoping by decreasing speed
    degree = 0
    line = 45
    for j in range(0, 6 + 1, 1):  #loop draw all the circles
        draw.penup()
        draw.forward(60)
        draw.pendown()
        for i in range(1, 360 + 1, 1):  #loop to draw an independant circle
            draw.forward(1)
            draw.right(1)  #changing arrowhead 1 degree in each iteration
        draw.penup()
        draw.home()
        draw.pendown()
        draw.right(t1)
        line = line + 52
        draw.right(line)
        draw.forward(100)  #a line with every circle
        draw.penup()
        draw.home()
        draw.pendown()
        draw.right(t1)
        degree = degree + 52
        draw.right(degree)

