import sys
from collections import deque
N=int(sys.stdin.readline().rstrip())
graph=[]
visit=[[False for _ in range(N)] for _ in range(N)]
for i in range(N):
    graph.append(list(sys.stdin.readline().rstrip()))
cnt=0
def bfs(i,j):
    global cnt
    if visit[i][j]==True:
        return
    q=deque()
    q.append((i,j))
    visit[i][j]=True
    dx=[-1,0,1,0]
    dy=[0,1,0,-1]
    while q:
        x,y=q.popleft()
        for i in range(4):
            cx=x+dx[i]
            cy=y+dy[i]
            if cx<0 or cx>=N or cy<0 or cy>=N:
                continue
            if graph[x][y]==graph[cx][cy] and visit[cx][cy]==False:
                q.append((cx,cy))
                visit[cx][cy]=True
    cnt+=1

for i in range(N):
    for j in range(N):
        bfs(i,j)
print(cnt, end=' ')
cnt=0
visit=[[False for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if graph[i][j]=='R':
            graph[i][j]='G'
for i in range(N):
    for j in range(N):
        bfs(i,j)
print(cnt)

