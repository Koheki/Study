N = int(input())
A = [int(n) for n in input().split()]
B = [int(n) for n in input().split()]

ans = 0 

for i in range(N):
    ans += 1/3*(A[i]) +2/3*(B[i])

print(ans)