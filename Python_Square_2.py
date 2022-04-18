import turtle
rsw = turtle.Turtle()
rsw.shape('turtle')

#variable definitions
distance_1 = 100
distance_2 = 200
angle_1 = 90

#first square
#go west then turn south
rsw.forward(distance_1)
rsw.right(angle_1)

#go south then turn east
rsw.forward(distance_1)
rsw.right(angle_1)

#go east then turn north
rsw.forward(distance_1)
rsw.right(angle_1)

#go north then turn west
rsw.forward(distance_1)
rsw.right(angle_1)

#second square
#go twice the distance then turn south
rsw.forward(distance_2)
rsw.right(angle_1)

#go south then turn east
rsw.forward(distance_1)
rsw.right(angle_1)

#go east then turn south
rsw.forward(distance_2)
rsw.left(angle_1)

#go south then turn west
rsw.forward(distance_1)
rsw.left(angle_1)

#go west then turn north
rsw.forward(distance_1)
rsw.left(angle_1)

#go north then turn west
rsw.forward(distance_1)
rsw.right(angle_1)

#go west then turn south
rsw.forward(distance_1)
rsw.right(angle_1)

#go south then turn east
rsw.forward(distance_1)
rsw.right(angle_1)

#go east and finish
rsw.forward(distance_1)
