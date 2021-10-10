import random
flag = True

a = random.randint(1,100)
b = random.randint(1,100)



while flag:
    count = random.randint(1,2)
    a = random.randint(1,100)
    b = random.randint(1,100)
    if count==1:
        answer = int(input(f"{a} + {b} = "))
        if answer==a+b:
            print("good!")
            flag = False     
        else:
            print("I'm sorry,, but keep try you can do it!")
    else:
        answer = int(input(f"{a} - {b} = "))
        if answer==a-b:
            print("good!")
            flag = False     
        else:
            print("I'm sorry,, but keep try you can do it!")

