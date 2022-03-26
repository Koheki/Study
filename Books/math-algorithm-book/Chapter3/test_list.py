
N = 10
W = 20

# inf = inf = -float("inf")

dp1 = [[0]*(W+1) for _ in range(N+1)]
dp2 = [[0]*(W+1)]* (N+1)


def tmp(dp):
    for i in dp:
        print(i)

    return "\n"

print(tmp(dp1))
print(tmp(dp2))