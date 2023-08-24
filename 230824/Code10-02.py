import numpy as np
## 넘파이 2차원 배열 생성
SIZE = 5
numpyAry = np.random.randint(0, 255, size=(SIZE, SIZE))

## 배열을 출력하기
print(numpyAry)
print()

## 배열에 100을 더하기.
numpyAry += 100

## 배열을 출력하기
print(numpyAry)