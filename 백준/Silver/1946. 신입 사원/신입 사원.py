import sys
T=int(sys.stdin.readline().rstrip())
for i in range(T):
    N=int(sys.stdin.readline().rstrip())
    lst=[]
    for j in range(N):
        a,b=map(int,sys.stdin.readline().strip().split())
        lst.append([a,b])
    cnt=1
    lst.sort(key=lambda x: x[0])
    best=lst[0][1]
    for k in range(1,N):
        if lst[k][1]< best:
            cnt+=1
            best=lst[k][1]
    print(cnt)

        