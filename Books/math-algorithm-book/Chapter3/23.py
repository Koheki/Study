N = int(input())
B = [int(n) for n in input().split()]
R = [int(n) for n in input().split()]

print(sum(B)/N + sum(R)/N)