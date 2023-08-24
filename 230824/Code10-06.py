import numpy as np
SIZE = 5  # 원본 크기
startRow,startCol = 1, 1 # 새로운 리스트의 시작 위치
nSIZE = 3 # 새로운 리스트의 크기

## 넘파이 2차원 배열 생성
value = 1
myAry1 = np.arange(value, value+(SIZE*SIZE), 1)
myAry1 = myAry1.reshape(SIZE, SIZE)

## 넘파이 2차원 배열 리스트의 출력
for i in range(SIZE) :
    [ print("%3d" % myAry1[i][k], end=' ') for k in range(SIZE) ]
    print()
print()

## 넘파이 2차원 배열의 슬라이싱
myAry2 = myAry1[startRow:startRow+nSIZE, startCol: startCol+nSIZE].copy()

## 넘파이 2차원 배열의 출력
for i in range(nSIZE) :
    [ print("%3d" % myAry2[i][k], end=' ') for k in range(nSIZE) ]
    print()
print()
