import random
## 파이썬 2차원 리스트 생성
SIZE = 5
pythonList = [ [random.randint(0,255) for _ in range(SIZE)] for _ in range(SIZE)]

## 리스트를 출력하기
for i in range(SIZE) :
    for k in range(SIZE) :
        print("%3d" % pythonList[i][k], end=' ')
    print()
print()

## 리스트에 100을 더하기.
for i in range(SIZE) :
    for k in range(SIZE) :
        pythonList[i][k] += 100

## 리스트를 출력하기
for i in range(SIZE) :
    for k in range(SIZE) :
        print("%3d" % pythonList[i][k], end=' ')
    print()