import turtle
c=("red","yellow","green","blue","white","purple")
t=turtle.Turtle()
screen=turtle.Screen()
screen.bgcolor("black")
t.speed(10)
for i in range(100):
    t.color(c[i % 6])
    t.forward(i*4)
    t.left(150)
    t.width(2)