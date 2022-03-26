import math

N = int(input())
A = [ int(n) for n in input().split()]

Count = {x:0 for x in range(1,100000)}
ans = 0

for a in A:
    Count[a] += 1

for i in range(1,50000):
    j = 100000 - i
    ans += Count[i]*Count[j]

ans += Count[50000]*(Count[50000]-1)//2

# h = Count[50000]
# if h > 1:
#     ans += math.factorial(h)//(math.factorial(h-2)*2)

print(ans)

