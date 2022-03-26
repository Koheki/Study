import math

N = int(input())

for i in range(1,int(math.sqrt(N))+1):
    if N % i == 0:
        print(i)
        print(N//i)
