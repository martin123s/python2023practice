import random
import turtle as t

obj = t.Turtle()
obj.shape("classic")
obj.width(10)


# turn the obj to the left down starting position.
def turn_left_down():
    obj.right(180)
    obj.penup()
    obj.forward(300)
    obj.left(90)
    obj.forward(290)
    obj.pendown()
    obj.left(90)


# draw a single circle with random color.
def draw_circle():
    R = random.random()
    G = random.random()
    B = random.random()
    obj.pencolor((R, G, B))
    obj.circle(5)


# back to left most start point
def start_point():
    obj.left(90)
    obj.penup()
    obj.forward(30)
    obj.left(90)
    obj.forward(600)
    obj.right(180)
    obj.pendown()


# 20 circle each line, and 20 lines
def one_line():
    for _ in range(20):
        obj.speed("fastest")
        draw_circle()
        obj.penup()
        obj.forward(30)
        obj.pendown()


def game():
    turn_left_down()
    for _ in range(20):
        one_line()
        start_point()


# play the game, and forming the 1 million dollars painting
game()


sc = t.Screen()
sc.exitonclick()