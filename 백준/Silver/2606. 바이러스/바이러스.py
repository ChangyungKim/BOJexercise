import sys
from collections import deque
cnt=0
N=int(sys.stdin.readline().rstrip())
M=int(sys.stdin.readline().rstrip())
graph=[[] for _ in range(N+1)]
visit=[False for _ in range(N+1)]
for i in range(M):
    a,b=map(int, sys.stdin.readline().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(v):
    global cnt
    q=deque()
    q.append(v)
    visit[v]=True
    while q:
        v=q.popleft()
        cnt+=1
        for i in graph[v]:
            if visit[i]==False:
                q.append(i)
                visit[i]=True
bfs(1)
print(cnt-1)
