import numpy as np
SIZE = 5  # 원본 크기

## 넘파이 2차원 배열 생성
imageAry = np.random.randint(0, 255, size=(SIZE, SIZE))
print('### 1. 원본 ###')
print(imageAry)
np.save('source', imageAry)

## (1) 10 증가후 저장
imageAry += 10
print('### 2. 10 증가 ###')
print(imageAry)
np.save('result1', imageAry)

##  (2) 흑백 처리후 저장
imageAry = np.where( imageAry<128, 0, 255)
print('### 3. 흑백 처리 ###')
print(imageAry)
np.save('result2', imageAry)

##  (3) 반전 처리후 저장
imageAry = 255 - imageAry
print('### 4. 반전 처리 ###')
print(imageAry)
np.save('result3', imageAry)

## 복구1 ##
imageAry = np.load('result2.npy')
print('### 복구1 : result2.npy ###')
print(imageAry)

## 복구2 ##
imageAry = np.load('result1.npy')
print('### 복구2 : result1.npy ###')
print(imageAry)

## 복구3 ##
imageAry = np.load('source.npy')
print('### 복구3(원본) : source.npy ###')
print(imageAry)