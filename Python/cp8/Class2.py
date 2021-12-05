class Cat:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def setName(self,name):
        self.name = name
    def getName(self):
        return self.name
    def __str__(self):
        a = f"({self.name},{self.age})"
        return a

missy = Cat('Missy',3)
lucky = Cat('Lucky',5)
print(missy)
print(lucky)
