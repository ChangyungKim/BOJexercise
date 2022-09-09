import sys
n=int(sys.stdin.readline().rstrip())
lst=[]
for i in range(n):
    lst.append(list(map(int, sys.stdin.readline().rstrip().split())))
for i in range(1,n):
    for j in range(i+1):
        if j==0:
            lst[i][j]=lst[i-1][j]+lst[i][j]
        elif i==j:
            lst[i][j]=lst[i][j]+lst[i-1][j-1]
        else:
            lst[i][j]=max(lst[i-1][j-1]+lst[i][j], lst[i-1][j]+lst[i][j])
print(max(lst[n-1]))
