import sys
N=int(sys.stdin.readline().rstrip())
lst=list(map(int, sys.stdin.readline().rstrip().split()))
count=0
for num in lst:
    if num==1:
        count+=1
    else:
        for i in range(2,num):
            if num%i==0:
                count+=1
                break
print(N-count)
        