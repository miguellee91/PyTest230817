import random
SIZE = 5  # 원본 크기
startRow,startCol = 1, 1 # 새로운 리스트의 시작 위치
nSIZE = 3 # 새로운 리스트의 크기

## 파이썬 2차원 리스트 생성
value = 1
myList1 = [ ]
for _ in range(SIZE)  :
    tmpList= []
    for _ in range(SIZE) :
        tmpList.append(value)
        value += 1
    myList1.append(tmpList)

## 파이썬 2차원 리스트의 출력
for i in range(SIZE) :
    [ print("%3d" % myList1[i][k], end=' ') for k in range(SIZE) ]
    print()
print()

## 파이썬 2차원 리스트의 슬라이싱
myList2 = []
for i in range(startRow, startRow+nSIZE) :
    tmpList = []
    for k in range(startCol, startCol+nSIZE) :
        tmpList.append(myList1[i][k])
    myList2.append(tmpList)

## 파이썬 2차원 리스트의 출력
for i in range(nSIZE) :
    [ print("%3d" % myList2[i][k], end=' ') for k in range(nSIZE) ]
    print()
print()