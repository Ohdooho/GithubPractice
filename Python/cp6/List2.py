select = 0
friends = []

while select !=9:
    print("-------------------")
    print("1.친구 리스트 출력")
    print("2.친구 추가")
    print("3.친구 삭제")
    print("4.이름 변경")
    print("9.종료")
    select = int(input("메뉴를 선택하세요:"))
    if select ==1:
        if len(friends)==0:
            print("친구가 없습니다!")
            continue
        else :
            print(friends)
    elif select==2:
        new = input("이름을 입력하세요:")
        friends.append(new)
    elif select==3:
        out = input("지울 친구의 이름을 입력하세요:")
        friends.remove(out)
    elif select==4:
        old_name = input("변경 하고싶은 친구의 이름을 입력하세요:")
        if old_name in friends:
            index = friends.index(old_name)
            new_name = input("새로운 친구의 이름을 입력하세요:")
            friends[index]=new_name
        else:
            print("친구 리스트에 존재하지 않는 이름입니다.")
    elif select==9:
        break
    else:
        continue
            