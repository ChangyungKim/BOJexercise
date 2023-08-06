import sys
T=int(sys.stdin.readline().rstrip())
dp=[0]*91
dp[1]=1
dp[2]=1
for i in range(2,T+1):
    dp[i]=dp[i-1]+dp[i-2]
print(dp[T])
