import sys
N=int(sys.stdin.readline().rstrip())
lst=list(map(int, sys.stdin.readline().rstrip().split()))
lst.sort()
min=300000
for i in range(N):
    if min>lst[i]+lst[2*N-1-i]:
        min=lst[i]+lst[2*N-1-i]
print(min)
