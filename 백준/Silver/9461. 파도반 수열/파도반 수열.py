import sys
dp=[0 for _ in range(101)]
dp[1]=1
dp[2]=1
dp[3]=1
for i in range(4,101):
    dp[i]=dp[i-2]+dp[i-3]
T=int(sys.stdin.readline().rstrip())
for i in range(T):
    N=int(sys.stdin.readline().rstrip())
    print(dp[N])
