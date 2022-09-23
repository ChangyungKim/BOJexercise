import sys, heapq
hq=[]
N=int(sys.stdin.readline().rstrip())
for i in range(N):
    x=int(sys.stdin.readline().rstrip())
    if x>0:
        heapq.heappush(hq,(-x,x))
    else:
        if not hq:
            print(0)
        else:
            print(heapq.heappop(hq)[1])