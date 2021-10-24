import turtle

def drawBar(height):
    t.begin_fill()
    t.left(90)
    t.forward(height)
    t.write(str(height),font = ('Times new Roman',16,'bold'))
    t.right(90)
    
    t.fd(40)
    t.rt(90)
    t.fd(height)
    t.lt(90)
    t.end_fill()
    
data = [120,56,309,220,156,23,98]

t = turtle.Turtle()
t.color("blue")
t.fillcolor("red")

t.pensize(3)

for d in data:
    drawBar(d)
    





turtle.mainloop()
turtle.bye()