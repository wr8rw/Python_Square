import turtle
rsw = turtle.Turtle()
rsw.shape('turtle')

size = 40
angle = 90

#defining function "square" here
def square(myColor, x, y):
   rsw.color(myColor)
   rsw.penup()
   rsw.goto(x, y)
   rsw.pendown()
   for i in range(4):
      rsw.forward(size)
      rsw.right(angle)
   
#Building the squares here  
square('red', -50, 80)
square('orange', 50, 70)
square('green', -50, -20)
square('blue', 70, -50)
