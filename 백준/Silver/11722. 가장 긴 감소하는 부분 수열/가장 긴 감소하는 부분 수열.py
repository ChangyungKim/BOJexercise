import sys
N=int(sys.stdin.readline().rstrip())
A=list(map(int, sys.stdin.readline().rstrip().split()))
dp=[1]*N
for i in range(len(A)):
    for j in range(i):
        if A[i]<A[j]:
            dp[i]=max(dp[i], dp[j]+1)
print(max(dp))