# AC
from sys import stdin

T = int(stdin.readline())

for i in range(T):
    count = 0
    flag = False

    operator = stdin.readline()
    size = int(stdin.readline())
    pList = stdin.readline()
    
    if size == 0:
        pList = []
    else:
        pList = list(map(int, pList[1:-2].split(",")))
        
    for j in operator:
        if j == 'R':
            count += 1
        if j == 'D':
            if size == 0:
                print("error")
                flag = True
                break
            else:
                if count%2 == 0:
                    pList.pop(0)
                else:
                    pList.pop()
                size -= 1

    if not flag:
        if count%2 != 0:
            pList.reverse()
        # print(pList)
        print('[', end="")
        for k in range(size):
            if k == size-1:
                print(pList[k], end="")
            else:
                print(pList[k], end=",")
        print(']')