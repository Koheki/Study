import math

N = int(input())
Num = N
ans = []

for i in range(2,int(math.sqrt(N))+1):
    while Num % i == 0:
            ans.append(str(i))
            Num //= i
    
if Num != 1:
    ans.append(str(Num))


print(" ".join(ans))




