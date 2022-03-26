N = int(input())
A = list(map(int,input().split()))

Count = {100:0,200:0,300:0,400:0}

for a in A:
    Count[a] += 1

print(Count[100]*Count[400]+Count[200]*Count[300])

