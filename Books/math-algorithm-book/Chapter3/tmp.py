
def fruc(n):
    if n == 1:
        return 1
    else:
        return fruc(n-1) * n

print(fruc(5))