def menu():
    print("1.연락처 추가")
    print("2.연락처 삭제")
    print("3.연락처 검색")
    print("4.연락처 출력")
    print("5.종료")

def get_contact():
    name=input("이름:")
    contact=input("전화번호:")
    return name,contact
def main():
    addressbook = {}
    a = 0
    while(a!=5):
        menu()
        a = int(input("메뉴를 입력하세요:"))
        if a==1:
            key,value=get_contact()
            addressbook[key]=value
        if a==2:
            key=input("삭제할 사람의 이름을 입력하세요:")
            addressbook.pop(key)
        if a==3:
            key=input("찾으시는 분의 이름을 입력하세요:")
            if key in addressbook:
                print("전화번호:",addressbook[key])
            else:
                print("존재하지 않는 연락처입니다.")
        if a==4:
            for key in sorted(addressbook):
                print("이름:",key," 전화번호:",addressbook[key])

main()





