import turtle
import random
t=turtle.Turtle()
t.shape("turtle")

for i in range(1,11):
    r = random.randint(1,100)
    x = random.randint(1,100)
    y = random.randint(1,100)
    t.circle(r)
    t.penup()
    t.goto(x,y)
    t.pendown()




turtle.mainloop()
turtle.bye()