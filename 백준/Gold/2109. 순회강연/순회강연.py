import sys
from queue import PriorityQueue
sum=0
N=int(sys.stdin.readline().rstrip())
lst=[[0 for _ in range(2)] for _ in range(N)]
for i in range(N):
    lst[i][0], lst[i][1]=map(int, sys.stdin.readline().rstrip().split())
lst.sort(key=lambda x : x[1])
q=PriorityQueue()
for i in lst:
    q.put(i[0])
    if q.qsize()>i[1]:
        q.get()
for i in range(q.qsize()):
    sum+=q.get()
print(sum)