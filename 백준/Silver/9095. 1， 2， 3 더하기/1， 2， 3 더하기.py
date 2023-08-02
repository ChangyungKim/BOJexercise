import sys
T=int(sys.stdin.readline().rstrip())
dp=[0]*11
dp[1]=1
dp[2]=2
dp[3]=4
for i in range(T):
    n=int(sys.stdin.readline().rstrip())
    for j in range(4, n+1):
        dp[j]=dp[j-1]+dp[j-2]+dp[j-3]
    print(dp[n])
