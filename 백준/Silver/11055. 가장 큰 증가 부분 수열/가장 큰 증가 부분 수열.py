import sys
N=int(sys.stdin.readline().rstrip())
A=list(map(int, sys.stdin.readline().rstrip().split()))
dp=A[:]
for i in range(N):
    for j in range(i):
        if A[i]>A[j]:
            dp[i]=max(dp[i], dp[j]+A[i])
print(max(dp))