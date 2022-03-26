N = int(input())
A = list(map(int,input().split()))

a = A.count(1)
b = A.count(2)
c = A.count(3)

print(a*(a-1)//2+b*(b-1)//2+c*(c-1)//2)