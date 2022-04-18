import turtle
rsw = turtle.Turtle()
rsw.shape('turtle')

distance = 100
angle = 90

for i in range(1, 5):
   if i > 2: # true if i greater than 2
      rsw.color('red')
      rsw.pensize(5)
   else: # if i is exactly 2 or less than 2
      rsw.color('blue')
      rsw.pensize(3)
   rsw.forward(distance)
   rsw.right(angle)
