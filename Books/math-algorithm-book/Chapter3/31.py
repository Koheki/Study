N = int(input())
A = [int(n) for n in input().split()]

dp1 = [0]*(N+1)
dp2 = [0]*(N+1)

for i in range(1,N+1):
    # i日目に勉強する
    dp1[i] = dp2[i-1]+A[i-1]

    # i日目に勉強しない
    dp2[i] = max(dp1[i-1],dp2[i-1])


print(max(dp1[N],dp2[N]))
