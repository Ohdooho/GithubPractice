import random

init = 50

target = 250

count = 0
for i in range(100):   
    cash = init
    while cash >0 and cash <target:
        cash = cash-1
        win = random.randint(1,2)
        if win ==1:
            cash = cash+2
            if cash==target:
                count +=1
        else :
                continue

print("초기금액 ",init)
print("목표 금액 ",target)            
print("100번중에 ,",count,"번 성공 ")