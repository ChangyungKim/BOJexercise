import sys
N=int(sys.stdin.readline().rstrip())
lst=[]
for i in range(N):
    lst.append(list(map(int, sys.stdin.readline().rstrip().split())))
for i in range(N):
    print(1+sum(1 for j in range(N) if lst[j][0]>lst[i][0] and lst[j][1]>lst[i][1]))
