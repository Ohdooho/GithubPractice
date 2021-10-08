import random

a = random.randint(1,10)
b = random.randint(1,10)

c = random.randint(1,4)

if c ==1 :
    answer=int(input(f"{a} + {b} 의 값은? "))
    if answer == a+b:
        print("맞았습니다.")
    else:
        print("틀렸습니다.")
if c ==2 :
    answer=int(input(f"{a} - {b} 의 값은? "))
    if answer == a-b:
        print("맞았습니다.")
    else:
        print("틀렸습니다.")
if c ==3 :
    answer=int(input(f"{a} * {b} 의 값은? "))
    if answer == a*b:
        print("맞았습니다.")
    else:
        print("틀렸습니다.")
if c ==4 :
    answer=int(input(f"{a} / {b} 의 값은? "))
    if answer == a/b:
        print("맞았습니다.")
    else:
        print("틀렸습니다.")
