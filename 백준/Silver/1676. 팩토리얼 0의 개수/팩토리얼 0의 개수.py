import sys

N=1
n=int(sys.stdin.readline().rstrip())
for i in range(1,n+1):
    N*=i
cnt=0
while True:
    if N%10!=0:
        break
    else:
        cnt+=1
        N=N//10
print(cnt)
