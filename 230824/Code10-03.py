import numpy as np
import random

pythonList = [ random.randint(0,255) for _ in range(5)]
print('* 파이썬 리스트 --> ', pythonList)

numpyAry1 = np.array(pythonList)
print('* array(pythonList) --> ', numpyAry1)

numpyAry2 = np.arange(5)
print('* arange(5) --> ', numpyAry2)
numpyAry3 = np.arange(3, 8)
print('* arange(3, 8) --> ', numpyAry3)
numpyAry3 = np.arange(0, 100, 20)
print('* arange(0, 100, 20) --> ', numpyAry3)

numpyAry4 = np.ones(5)
print('* ones(5) --> \n', numpyAry4)
numpyAry5 = np.ones((3,4))
print('* ones((3,4)) )--> \n', numpyAry5)

numpyAry6 = np.zeros(5)
print('* zeros(5)--> ', numpyAry6)

numpyAry7 = np.empty(6)
print('* empty(6)--> ', numpyAry7)

numpyAry8 = np.full(5, 33)
print('* full(5, 33) --> ', numpyAry8)

numpyAry9 = np.identity(5)
print('* identity(5)--> \n', numpyAry9)
