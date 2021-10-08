import turtle

t = turtle.Turtle()
t.shape("turtle")


s= turtle.textinput("", "도형을 입력하시오 :")

if s =="사각형" :
    w = int(turtle.textinput("","가로 : "))
    h = int(turtle.textinput("","세로 : "))
    t.fd(w)
    t.lt(90)
    t.fd(h)
    t.lt(90)
    t.fd(w)
    t.lt(90)
    t.fd(h)
    t.lt(90)
    
if s =="삼각형":
    l = int(turtle.textinput("","한 변의 길이? : "))
    t.fd(l)
    t.lt(120)
    t.fd(l)
    t.lt(120)
    t.fd(l) 
if s =="원":
    r = int(turtle.textinput("","반지름? : "))
    t.circle(r)
    