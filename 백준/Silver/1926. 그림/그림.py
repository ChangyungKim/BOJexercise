import sys
from collections import deque
n,m=map(int, sys.stdin.readline().rstrip().split())
graph=[]
result=[0]
cnt=0
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip().split())))

def bfs(x,y):
    if graph[x][y]==0:
        return
    dx=[-1,0,1,0]
    dy=[0,1,0,-1]
    global cnt
    counting=0
    q=deque()
    q.append((x,y))
    graph[x][y]=0
    while q:
        x,y=q.popleft()
        counting+=1
        for i in range(4):
            cx=x+dx[i]
            cy=y+dy[i]
            if cx<0 or cx>=n or cy<0 or cy>=m:
                continue
            if graph[cx][cy]==1:
                q.append((cx,cy))
                graph[cx][cy]=0
    result.append(counting)
    cnt+=1

for i in range(n):
    for j in range(m):
        bfs(i,j)
print(cnt)
print(max(result))
