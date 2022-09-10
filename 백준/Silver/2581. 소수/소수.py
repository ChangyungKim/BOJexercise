import sys
lst=[]

def prime_num(n):
    flag=0
    if n>1:
        for i in range(2,n):
            if n%i==0:
                flag=1
                break
        if flag==0:
            lst.append(n)
    

M=int(sys.stdin.readline().rstrip())
N=int(sys.stdin.readline().rstrip())
for i in range(M,N+1):
    prime_num(i)
if len(lst)==0:
    print(-1)
else:
    print(sum(lst))
    print(lst[0])