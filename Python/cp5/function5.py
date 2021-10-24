import turtle


t=turtle.Turtle()
t.shape("turtle")

def draw_line(angle):
    for i in range(1,13):    
        t.fd(100)
        t.backward(100)
        t.lt(angle)
        
def main():
    angle=30
    draw_line(angle)


main()


turtle.mainloop()
turtle.bye()