import turtle

def draw():
    t = turtle.Turtle()
    window = turtle.Screen()
    t.color("black")
    t.speed(500)
    

    for i in range (1,500):
        if(i%3==0):
            t.forward(100)
            t.left (90)
        else:
            t.forward(100)
            t.right (90)
        if (i%12 ==0):
            t.right(10)


    window.exitonclick()
draw()
    