import sys

N = int(input())

array = list()

for i in range(N) :
    array.append(list(map(int, input().split())))

for i in range(N) :
    if i != 0 :
        print("")
    for j in range(1, N+1) :
        print(j, end=' ')
        