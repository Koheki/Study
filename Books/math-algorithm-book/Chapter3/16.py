N = int(input())
A = list(map(int,input().split()))


def gcd(a,b):
    while a > 0 and b > 0:
        if a > b:
            a %= b
        else:
            b %= a
    return max(a,b)

cd = A[0]

for i in range(1,N):
    cd = gcd(cd,A[i])


print(cd)

