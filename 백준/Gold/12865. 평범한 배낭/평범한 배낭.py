import sys
N,K=map(int,sys.stdin.readline().rstrip().split())
lst=[[0,0]]
dp=[[0 for _ in range(K+1)] for _ in range(N+1)]
for i in range(N):
    lst.append(list(map(int, sys.stdin.readline().rstrip().split())))
for i in range(1, N+1):
    for j in range(1,K+1):
        w=lst[i][0]
        v=lst[i][1]

        if j<w:
            dp[i][j]=dp[i-1][j]
        else:
            dp[i][j]=max(dp[i-1][j-w]+v, dp[i-1][j])
print(dp[N][K])
