import sys
from collections import deque
N=int(sys.stdin.readline().rstrip())
lst=deque([i for i in range(1,N+1)])
while len(lst)!=1:
    lst.popleft()
    num=lst.popleft()
    lst.append(num)
print(lst[0])