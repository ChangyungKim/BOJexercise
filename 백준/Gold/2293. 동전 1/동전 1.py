import sys
n,k=map(int,sys.stdin.readline().rstrip().split())
coin=[]
for i in range(n):
    coin.append(int(sys.stdin.readline().rstrip()))
dp=[1]+[0]*(k)
for i in coin:
    for j in range(1,k+1):
        if j>=i:
            dp[j]+=dp[j-i]
print(dp[k])
