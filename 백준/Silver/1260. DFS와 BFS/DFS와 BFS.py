import sys
from collections import deque
sys.setrecursionlimit(20000)
N,M,V=map(int, sys.stdin.readline().rstrip().split())
graph=[[] for _ in range(N+1)]
visit1=[False for _ in range(N+1)]
visit2=[False for _ in range(N+1)]
for i in range(M):
    a,b=map(int, sys.stdin.readline().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)
    
def dfs(v):
    if visit1[v]:
        return
    visit1[v]=True
    print(v, end=' ')
    graph[v].sort()
    for i in graph[v]:
        dfs(i)

def bfs(v):
    q=deque()
    q.append(v)
    visit2[v]=True
    while q:
        s=q.popleft()
        print(s, end=' ')
        graph[s].sort()
        for i in graph[s]:
            if visit2[i]==False:
                q.append(i)
                visit2[i]=True
dfs(V)
print()
bfs(V)

