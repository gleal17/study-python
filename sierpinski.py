import turtle

def draw_triangle(vertices,color,my_turtle):
    my_turtle.fillcolor(color)
    my_turtle.up()
    my_turtle.goto(vertices[0][0],vertices[0][1])
    my_turtle.down()
    my_turtle.begin_fill()
    my_turtle.goto(vertices[1][0],vertices[1][1])
    my_turtle.goto(vertices[2][0],vertices[2][1])
    my_turtle.goto(vertices[0][0],vertices[0][1])
    my_turtle.end_fill()
    
def midpoint(point1, point2):
    return [(point1[0] + point2[0])/2, (point1[1] + point2[1])/2]
    

def draw_fractal(vertices,level,my_turtle):

    colors = [(0,150,189),(4,150,116),(216,95,30),(193,33,57),(129,41,199),
                (102,205,135),(51,187,204)]
    draw_triangle(vertices,colors[level],my_turtle)
   
    if level > 0:

        draw_fractal([vertices[0],
                      midpoint(vertices[0], vertices[1]),
                      midpoint(vertices[0], vertices[2])],
                      level - 1, my_turtle)
        draw_fractal([vertices[1],
                      midpoint(vertices[0], vertices[1]),
                      midpoint(vertices[1], vertices[2])],
                      level - 1, my_turtle)
        draw_fractal([vertices[2],
                      midpoint(vertices[2], vertices[1]),
                      midpoint(vertices[0], vertices[2])],
                      level - 1, my_turtle)

my_turtle = turtle.Turtle()
my_turtle.shape('turtle')
screen = turtle.Screen()
screen.colormode(255) 
vertices = [[-200, -100], [0, 200], [200, -100]]
level = 4
draw_fractal(vertices, level, my_turtle)
screen.exitonclick()