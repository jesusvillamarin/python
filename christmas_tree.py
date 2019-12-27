'''
    Autor: JESÚS AURIOL VILLAMARÍN ORTIZ
    DATE: 28/11/2019
    DESCRIPTION: HOW TO EXECUTE PYTHON PROGRAM, COURSERA VIDEO 1.1.5
'''
#Codigo extraido de: https://gist.github.com/jurandysoares/4380835
'''
    Other commands to use of turtle package
    > turtle.colormode(5)
    > turtle.pensize(10)
    > turtle.fillcolor("blue")
    > turtle.begin_fill()
    > turtle.goto(100, 0)
    > turtle.goto(100, 100)
    > turtle.goto(0, 100)
    > turtle.goto(0, 0)
    > turtle.end_fill()
    > turtle.showturtle()
    > turtle.hideturtle()
    ...
    more in http://www.mclibre.org/consultar/python/lecciones/python-turtle-1.html#
'''
import turtle

screen = turtle.Screen()
screen.setup(800,600)

circle = turtle.Turtle()
circle.shape('circle')
circle.color('red')
circle.speed('fastest')
circle.up()

square = turtle.Turtle()
square.shape('square')
square.color('green')
square.speed('fastest')
square.up()

circle.goto(0,280)
circle.stamp()

k = 0
for i in range(1, 17):
    y = 30*i
    for j in range(i-k):
        x = 30*j
        square.goto(x,-y+280)
        square.stamp()
        square.goto(-x,-y+280)
        square.stamp()

    if i % 4 == 0:
        x =  30*(j+1)
        circle.color('red')
        circle.goto(-x,-y+280)
        circle.stamp()
        circle.goto(x,-y+280)
        circle.stamp()        
        k += 2

    if i % 4 == 3:
        x =  30*(j+1)
        circle.color('yellow')
        circle.goto(-x,-y+280)
        circle.stamp()
        circle.goto(x,-y+280)
        circle.stamp() 

square.color('brown')
for i in range(17,20):
    y = 30*i
    for j in range(3):    
        x = 30*j
        square.goto(x,-y+280)
        square.stamp()
        square.goto(-x,-y+280)
        square.stamp()        
        
turtle.exitonclick()