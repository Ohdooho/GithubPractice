number = int(input("정수 = "))

first = number%10
number = number//10
second = number%10
number = number//10
third=number%10
number = number//10
forth= number%10

result = first+second+third+forth

print(result)


