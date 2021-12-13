class Rectangle:
    def __init__(self,x,y,w,h):
        self.x=x
        self.y=y
        self.w=w
        self.h=h
    def __str__(self):
        msg = f"좌표({self.x},{self.y}),너비({self.w}),높이({self.h})"
        return msg
    def setX(self,x):
        self.x = x
    def setY(self,y):
        self.y = y
    def setH(self,h):
        self.h = h
    def setW(self,w):
        self.w = w
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def getH(self):
        return self.h
    def getW(self):
        return self.w
    def getArea(self):
        return self.w * self.h
    def overlap(self,r):
        if(self.getX()-self.getW()/2>r.getW()/2-r.getX() and self.getW()/2 - self.getX()<r.getX()-r.getW()/2 and
            self.getH()/2 - self.getY()<r.getY()-r.getH()/2 and self.getY()-self.getH()/2>r.getH()/2 - r.getY()
        ):
            print("r1 과 r2 는 겹치지 않습니다.")
        else:
            print("r1 과 r2 는 겹칩니다.")


r1 = Rectangle(0,0,100,100)
r2 = Rectangle(10,10,100,100)
r1.overlap(r2)

