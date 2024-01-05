import turtle as t

dash = t.Turtle()
dash.shape("turtle")

for _ in range(15):
    dash.forward(10)
    dash.penup()
    dash.forward(10)
    dash.pendown()

screen = t.Screen()
screen.exitonclick()