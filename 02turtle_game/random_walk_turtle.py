import random
import turtle as t

walk = t.Turtle()
walk.shape("classic")


def random_color():
    R = random.random()
    B = random.random()
    G = random.random()
    return walk.pencolor((R, B, G))


def random_walk():
    walk.speed(10)
    walk.width(15)
    random_color()
    walk.forward(30)


pace = 200
for _ in range(pace):
    item = random.randint(0, 1)
    if item == 0:
        walk.left(90)
        random_walk()
    else:
        walk.right(90)
        random_walk()

sc = t.Screen()
sc.exitonclick()