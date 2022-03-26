N = int(input())

ans = [2]

for i in range(2,N+1):
    flag = 1
    for a in ans:
        if i%a == 0:
            flag = 0
            break
    if flag == 1:
        ans.append(i)

print(" ".join([ str(i) for i in ans]))
