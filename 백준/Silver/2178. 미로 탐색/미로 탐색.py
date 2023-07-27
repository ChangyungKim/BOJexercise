import sys
from collections import deque
graph=[]
N,M=map(int, sys.stdin.readline().rstrip().split())
for i in range(N):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))

def bfs(x,y):
    q=deque()
    q.append((x,y))
    dx=[-1,0,1,0]
    dy=[0,1,0,-1]
    while q:
        x,y=q.popleft()
        for i in range(4):
            cx=x+dx[i]
            cy=y+dy[i]
            if cx<0 or cx>=N or cy<0 or cy>=M:
                continue
            if graph[cx][cy]==1:
                graph[cx][cy]=graph[x][y]+1
                q.append((cx,cy))
bfs(0,0)
print(graph[N-1][M-1])
