N = int(input())
A = [ int(n) for n in input().split()]

def merge_sort(X):
    if len(X) == 1:
        print(X)
        return X

    m = len(X)//2
    A = merge_sort(X[0:m])
    B = merge_sort(X[m:len(X)])

    # Merge
    print(len(X),A,B)
    c1 = 0
    c2 = 0
    C = []
    while (c1 < len(A) or c2 < len(B)):
        if c1 == len(A):
            C.append(B[c2])
            c2 += 1
        elif c2 == len(B):
            C.append(A[c1])
            c1 += 1

        else:
            if A[c1] <= B[c2]:
                C.append(A[c1])
                c1 += 1
            else:
                C.append(B[c2])
                c2 += 1

    return C



ans = merge_sort(A)

print(*ans)