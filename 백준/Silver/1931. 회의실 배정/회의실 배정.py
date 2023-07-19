import sys
N=int(sys.stdin.readline().rstrip())
lst=[[0 for _ in range(2)] for _ in range(N)]
for i in range(N):
    lst[i][0], lst[i][1]=map(int, sys.stdin.readline().rstrip().split())
lst.sort(key=lambda x : (x[1], x[0]))
start=0
count=0
for i in range(N):
    if lst[i][0]>=start:
        count+=1
        start=lst[i][1]
print(count)