import sys
n=int(sys.stdin.readline().rstrip())
a,b=map(int, sys.stdin.readline().rstrip().split())
graph=[[]for _ in range(n+1)]
visit=[False for _ in range(n+1)]
m=int(sys.stdin.readline().rstrip())
result=[]
for i in range(m):
    c,d=map(int, sys.stdin.readline().rstrip().split())
    graph[c].append(d)
    graph[d].append(c)
def dfs(v,dep):
    if visit[v]==True:
        return
    dep+=1
    if v==b:
        result.append(dep)
    visit[v]=True
    for i in graph[v]:
        dfs(i,dep)

dfs(a,0)
if len(result)==0:
    print(-1)
else:
    print(result[0]-1)
        

