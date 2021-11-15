import random

game = []
counter = 1
xcounter = 0
for i in range(10):
    temp = random.randint(0,1)
    if temp==0:
        game.append(0)
    else:
        game.append(1)

        
for r in range(1,10):
    if game[r-1]==game[r]:
        counter+=1
    else:
        if xcounter>counter:
            counter = 1
        else:
            xcounter = counter
            counter = 1

if xcounter >=counter:
    counter = xcounter
print(game)
print("최대 연속 길이 :",counter)