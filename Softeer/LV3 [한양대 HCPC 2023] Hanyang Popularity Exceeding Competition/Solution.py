import sys

N = int(input())

ppl = 0
array = list()

for i in range(N) :
    array.append(list(map(int, sys.stdin.readline().split())))

for i in range(N) :
    if abs(array[i][0] - ppl) <= array[i][1] :
        ppl += 1
    else :
        continue

print(ppl)
