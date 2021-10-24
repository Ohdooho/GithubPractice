import turtle

t=turtle.Turtle()
t.shape("turtle")

def draw_square(size):
    if size<200:
        for i in range(4):
            t.fd(size)
            t.left(90)
            size = size +5
        draw_square(size)
    else:
        return 0
def main():
    size=1
    draw_square(size)
    
    
    
main()


turtle.mainloop()
turtle.bye()