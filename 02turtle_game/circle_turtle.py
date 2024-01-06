import random
import turtle as t

circle = t.Turtle()

# step by step to build the circle
# for i in range(360):
#     circle.speed("fastest")
#     circle.left(1)
#     circle.forward(1)


def circle_color():
    R = random.random()
    G = random.random()
    B = random.random()
    random_color = (R, G, B)
    return circle.pencolor(random_color)


def circle_pattern():
    for i in range(100):
        circle_color()
        circle.left(i)
        circle.speed("fastest")
        circle.circle(80)


circle_pattern()
sc = t.Screen()
sc.exitonclick()