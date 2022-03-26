N = int(input())
A = list(map(int,input().split()))


def lcm(a,b):
    t = a*b
    # gcd
    while a > 0 and b > 0:
        if a > b:
            a %= b
        else:
            b %= a
    # return lcm
    return t//max(a,b)

cm = A[0]

for i in range(1,N):
    cm = lcm(cm,A[i])

print(cm)

