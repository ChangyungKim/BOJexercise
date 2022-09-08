import sys
K,N=map(int, sys.stdin.readline().rstrip().split())
lst=[]
for i in range(K):
    lst.append(int(sys.stdin.readline().rstrip()))
e=max(lst)
s=1
while s<=e:
    m=(s+e)//2
    cnt=0
    for i in range(K):
        cnt+=lst[i]//m
    if cnt<N:
        e=m-1
    else:
        s=m+1
print(e)