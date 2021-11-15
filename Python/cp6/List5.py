import random

def print_List(mine):
    for r in range(len(mine)):
        for c in range(len(mine[0])):
            print(mine[r][c],end=" ")
        print()

mine = [["." for x in range(10)]for _ in range(10)]
for r in range(len(mine)):
    for c in range(len(mine[0])):
        temp = random.randint(1,10)
        if temp>7:
            mine[r][c] = "#"
            


print_List(mine)



