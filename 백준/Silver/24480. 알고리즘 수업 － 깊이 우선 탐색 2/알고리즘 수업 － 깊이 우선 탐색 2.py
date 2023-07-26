import sys
sys.setrecursionlimit(200000)
N,M,R=map(int, sys.stdin.readline().rstrip().split())
graph=[[] for _ in range(N+1)]
visit=[False for _ in range(N+1)]
result=[0 for _ in range(N+1)]
cnt=0
for i in range(M):
    a,b=map(int, sys.stdin.readline().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)
def dfs(v):
    global cnt
    if visit[v]:
        return
    graph[v].sort(reverse=True)
    visit[v]=True
    cnt+=1
    result[v]=cnt
    for i in graph[v]:
        dfs(i)

dfs(R)
for i in range(1,N+1):
    print(result[i])
