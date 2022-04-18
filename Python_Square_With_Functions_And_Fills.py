import turtle
rsw = turtle.Turtle()
rsw.shape('turtle')

distance = 100
angle = 120

#defining the function "petal" here
def petal():
   if i % 2:
      rsw.color('green')
   else:
      rsw.color('lightgreen')
   rsw.left(30)
   # draw a triangle and fill in the color
   rsw.begin_fill()
   rsw.forward(distance)
   rsw.right(angle)
   rsw.forward(distance)
   rsw.right(angle)
   rsw.forward(distance)
   rsw.end_fill()
   rsw.left(angle)

# start off 45 right
rsw.right(45)
# calling the function "petal" here
# repeat the forward/right functions four times
for i in range(4):
   petal()
# now draw the stem
rsw.pensize(10)
rsw.right(45)
rsw.forward(200)

rsw.write('done with flower')
