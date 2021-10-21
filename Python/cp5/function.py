def menu():
    print("1. 섭씨온도 -> 화씨온도")
    print("2. 화씨온도 -> 섭씨온도")
    print("3. 종료")
    select = int(input("메뉴를 선택하세요:"))
    return select
def ctof(c):
    temp = c*9.0/5.0 +32
    return temp
def ftoc(f):
    temp = (f-32.0)*5.0/9.0
    return temp

def input_1():
    a=float(input("섭씨 온도를 입력하세요:"))
    print("화씨온도 =",ctof(a))

def input_2():
    b = float(input("화씨 온도를 입력하세요:"))
    print("섭씨온도 =",ftoc(b))

def main():
    while(True):
        s=menu()
        if(s==1):
            input_1()
        elif(s==2):
            input_2()
        elif(s==3):
            break
        else:
            continue


main()