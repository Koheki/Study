n,r = map(int,input().split())

def factorial(a,b):
    if a <= b:
        return 1
    else:
        return a * factorial(a-1,b)

print(factorial(n,r)//factorial(n-r,1))
