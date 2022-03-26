import math

Num = int(input())
ans = []

while Num > 1:
    flag = 1

    for i in range(2,int(math.sqrt(Num))+1):
        if Num % i == 0:
            flag = 0
            ans.append(str(i))
            Num //= i
            break

    if flag:
        ans.append(str(Num))
        break

print(" ".join(ans))




