import sys
N=int(sys.stdin.readline().rstrip())
A=list(map(int, sys.stdin.readline().rstrip().split()))
lst=[0]
for i in range(len(A)):
    s=0;e=len(lst)
    if A[i]>lst[-1]:
        lst.append(A[i])
    else:
        while s<=e:
            m=(s+e)//2
            if lst[m]<A[i]:
                s=m+1
            else:
                e=m-1
        lst[s]=A[i]
print(len(lst)-1)
