def printlist(list):
    for row in range(len(list)):
        for col in range(len(list[0])):
            print(list[row][col],end=" ")
        print()


list1 = []
for row in range(10):
    list1+=[[0]*10]
while(True):
    print("---------------------")
    print("1 2 3 4 5 6 7 8 9 10")
    print("---------------------")
    printlist(list1)
    r = int(input("원하시는 좌석의 행 번호를 입력하세요 (종료는 -1): "))
    if r == -1:
        break
    c = int(input("원하시는 좌석의 열 번호를 입력하세요 (종료는 -1): "))
    if c == -1:
        break
    if list1[r-1][c-1]==1:
        print("이미 예약된 좌석입니다. 다른 좌석을 선택해주세요.")
        continue
    else:
        list1[r-1][c-1]=1
        print("예약되었습니다.")
