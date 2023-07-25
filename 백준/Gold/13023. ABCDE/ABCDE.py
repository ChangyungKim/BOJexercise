import sys
N,M=map(int, sys.stdin.readline().rstrip().split())
graph=[[]for _ in range(N)]
visit=[False for _ in range(N)]
cond=False
for i in range(M):
    a,b=map(int, sys.stdin.readline().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)
    
def dfs(i,dep):
    if dep==5:
        print(1)
        exit()
    for j in graph[i]:
        if visit[j]:
            continue
        visit[j]=True
        dfs(j,dep+1)
        visit[j]=False
for i in range(N):
    visit[i]=True
    dfs(i,1)
    visit[i]=False
print(0)
        
            
