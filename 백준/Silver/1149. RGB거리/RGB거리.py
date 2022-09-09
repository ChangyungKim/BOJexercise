import sys
N=int(sys.stdin.readline().rstrip())
lst=[]
for i in range(N):
    lst.append(list(map(int, sys.stdin.readline().rstrip().split())))
for j in range(1,N):
    lst[j][0]=min(lst[j-1][1], lst[j-1][2])+lst[j][0]
    lst[j][1]=min(lst[j-1][0], lst[j-1][2])+lst[j][1]
    lst[j][2]=min(lst[j-1][0], lst[j-1][1])+lst[j][2]
print(min(lst[N-1][0], lst[N-1][1], lst[N-1][2]))
