import turtle
def drawTree(branch,t):
    if(branch > 5):
        t.fd(branch)
        t.rt(20)
        drawTree(branch-15,t)
        t.lt(40)
        drawTree(branch-15,t)
        t.rt(20)
        t.backward(branch)

def main():
    t= turtle.Turtle()
    window = turtle.Screen()
    t.lt(90)
    t.up()
    t.backward(200)
    t.down()
    t.color("green")
    drawTree(100,t)
    window.exitonclick()


main()
