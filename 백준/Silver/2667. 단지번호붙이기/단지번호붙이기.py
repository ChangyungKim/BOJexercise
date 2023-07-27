import sys
from collections import deque
N=int(sys.stdin.readline().rstrip())
counting=0
result=[]
graph=[]
for i in range(N):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))
    
def bfs(x,y):
    if graph[x][y]==0:
        return
    global counting
    cnt=0
    q=deque()
    q.append((x,y))
    graph[x][y]=0
    dx=[-1,0,1,0]
    dy=[0,1,0,-1]
    while q:
        x,y=q.popleft()
        cnt+=1
        for i in range(4):
            cx=x+dx[i]
            cy=y+dy[i]
            if cx<0 or cx>=N or cy<0 or cy>=N:
                continue
            if graph[cx][cy]==1:
                q.append((cx,cy))
                graph[cx][cy]=0
    result.append(cnt)
    counting+=1

for i in range(N):
    for j in range(N):
        bfs(i,j)
result.sort()
print(counting)
for i in range(counting):
    print(result[i])
