N = int(input())
A = [ int(n) for n in input().split()]

def merge_sort(X):
    if len(X) <= 1:
        return X

    m = len(X)//2

    L = merge_sort(X[:m])
    R = merge_sort(X[m:])

    return merge(L,R)

def merge(L,R):
    merged = []
    l,r = 0,0

    while l < len(L) and r < len(R):

        if L[l] <= R[r]:
            merged.append(L[l])
            l += 1
        else:
            merged.append(R[r])
            r += 1

    if l < len(L):
        merged.extend(L[l:])
    if r < len(R):
        merged.extend(R[r:])

    return merged

ans = merge_sort(A)

print(*ans)