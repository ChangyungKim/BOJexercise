import sys
n,k=map(int,sys.stdin.readline().rstrip().split())
coin=[]
dp=[10001]*(k+1)
dp[0]=0
for i in range(n):
    num=int(sys.stdin.readline().rstrip())
    coin.append(num)
for j in coin:
    for i in range(j,k+1):
        dp[i]=min(dp[i], dp[i-j]+1)
if dp[k]==10001:
    print(-1)
else:
    print(dp[k])