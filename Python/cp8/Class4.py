class Person:
    def __init__(self,name,mobile="none",office="none",email="none"):
        self.__name = name
        self.__mobile = mobile
        self.__office = office
        self.__email = email
    def getName(self):
        return self.__name
    def getMobile(self):
        return self.__mobile
    def getOffice(self):
        return self.__office
    def getEmail(self):
        return self.__email
    def setName(self,n):
        self.__name = n
    def setMobile(self,m):
        self.__mobile = m
    def setOffice(self,o):
        self.__office = o
    def setEmail(self,e):
        self.__email = e
    def __str__(self):
        msg = f"({self.getName()}, office:{self.getOffice()}, mobile:{self.getMobile()}, Email:{self.getEmail()})"
        return msg



p1 = Person("Kim",office = "1234567",email ="kim@company.com")
p1.setMobile("01066378632")
p2 = Person("Park",office = "234567")
p2.setEmail("park@company.com")
print(p1)
print(p2)
