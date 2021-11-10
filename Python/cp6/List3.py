def printlist(list):
    rows = len(list)
    cols = len(list[0])
    for i in range(rows):
        print()
        for j in range(cols):
            print(list[i][j],end=",")



def init(list):
    rows = len(list)
    cols = len(list[0])

    for i in range(rows):
        for j in range(cols):
            if((i+j)%2==0):
                list[i][j]=1
            else:
                list[i][j]=0

def main():
    temp = []
    for row in range(10):
        temp +=[[0]*10]
    init(temp)

    printlist(temp)
main()