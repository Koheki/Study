N = int(input())
A = list(map(int,input().split()))

ans = 0

## 多分pypyで出さないと通らない(動的計画法で書けば回るっぽい)

for i1 in range(N):
    for i2 in range(i1+1,N):
        for i3 in range(i2+1,N):
            for i4 in range(i3+1,N):
                for i5 in range(i4+1,N):
                    if A[i1] + A[i2] + A[i3] + A[i4] + A[i5] == 1000:
                        ans+=1

print(ans)
