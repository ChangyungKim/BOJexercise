import sys
M,N=map(int, sys.stdin.readline().rstrip().split())
for num in range(M, N+1):
    flag=0
    if num==1:
        continue
    else:
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                flag=1
                break
        if flag==0:
            print(num)