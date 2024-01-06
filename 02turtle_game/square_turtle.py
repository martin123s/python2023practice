import turtle as t

user = t.Turtle()
user.shape("turtle")
user.color("red", "green")


for _ in range(4):
    user.speed(3)
    user.forward(200)
    user.left(90)

screen = t.Screen()
screen.exitonclick()