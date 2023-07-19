N=int(input())
result=0
a=list(map(int, input().split()))
a.sort()
for i in range(N):
    result+=(i+1)*(a[N-1-i])
print(result)