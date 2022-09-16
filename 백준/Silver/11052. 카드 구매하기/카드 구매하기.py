import sys
N=int(sys.stdin.readline().rstrip())
dp=[0]*(N+1)
P=list(map(int, sys.stdin.readline().rstrip().split()))
P.insert(0,0)
dp[1]=P[1]
for i in range(2,N+1):
    for j in range(1,i+1):
        dp[i]=max(dp[i], dp[i-j]+P[j])
print(dp[N])