import sys
from queue import PriorityQueue
N=int(sys.stdin.readline().rstrip())
card=PriorityQueue()
count=0
data1=0
data2=0
for i in range(N):
    card.put(int(sys.stdin.readline().rstrip()))
while card.qsize()!=1:
    data1=card.get()
    data2=card.get()
    count+=(data1+data2)
    card.put(data1+data2)
print(count)