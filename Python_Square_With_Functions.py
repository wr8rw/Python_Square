import turtle
rsw = turtle.Turtle()
rsw.shape('turtle')

distance = 50
angle = 90

# % = modulus operator...in other words the remainder of x divided by y

# function "side" defined here
def side():
   # if event then red 2, 4 etc.
   if i % 2:
      rsw.color('red')
   # else if odd then draw blue 1, 3 etc.
   else:
      rsw.color('blue')
   rsw.forward(distance)
   rsw.right(angle)

# function side "called" from this code
#repeat the forward/right functions four times
for i in range(4):
   side()

rsw.write('done with square')
