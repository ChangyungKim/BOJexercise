import sys
sys.setrecursionlimit(10000)
N,M=map(int, sys.stdin.readline().rstrip().split())
graph=[[] for _ in range(N+1)]
visit=[False for _ in range(N+1)]
for i in range(M):
    a,b=map(int, sys.stdin.readline().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)
def dfs(i):
    if visit[i]==True:
        return False
    visit[i]=True
    for j in graph[i]:
        if visit[j]==False:
            dfs(j)
    return True
cnt=0
for i in range(1,N+1):
    if dfs(i)==True:
        cnt+=1
print(cnt)
