N,S = map(int,input().split())
A = [int(a) for a in input().split()]

dp = [[0]*(S+1) for _ in range(N+1)]

for i in range(1,N+1):
    a = A[i-1]
    for j in range(S+1):
        if j < a:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j],dp[i-1][j-a]+a)

if dp[N][S] == S:
    print("Yes")
else:
    print("No")