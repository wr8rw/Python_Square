import turtle
rsw = turtle.Turtle()
rsw.shape('turtle')

#variable definitions
distance_1 = 100
distance_2 = 200
angle_1 = 90

#build square by looping
for i in range(4):
  rsw.forward(distance_1)
  rsw.right(angle_1)

rsw.left(angle_1)
rsw.forward(15)
rsw.write('Square Complete - Yay!!!!')
rsw.back(15)

  
