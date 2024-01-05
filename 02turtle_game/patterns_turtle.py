import random
import turtle as t

pattern = t.Turtle()
pattern.shape("classic")

'''
from triangle to other polygons
each angle of the pattern is:
angle = (n-2)*180/n
'''
for num in range(3, 11):
    angle = (num-2)*180/num
    R = random.random()
    B = random.random()
    G = random.random()
    pattern.pencolor((R, B, G))
    for _ in range(num):
        pattern.right(180-angle)
        pattern.speed(1)
        pattern.forward(70)

screen = t.Screen()
screen.exitonclick()