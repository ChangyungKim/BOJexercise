import sys
n=int(sys.stdin.readline().rstrip())
lst=[0]*1001
lst[0]=0
lst[1]=1
lst[2]=3
for i in range(3,n+1):
    lst[i]=(lst[i-1]+2*(lst[i-2]))%10007
print(lst[n])