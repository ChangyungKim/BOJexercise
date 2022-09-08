import sys
N=int(sys.stdin.readline().rstrip())
A=list(map(int, sys.stdin.readline().rstrip().split()))
B=[-1000000001]

for i in range(len(A)):
    if A[i]>B[-1]:
        B.append(A[i])
    else:
        s=0
        e=len(B)-1
        while s<=e:
            m=(s+e)//2
            if B[m]<A[i]:
                s=m+1
            else:
                e=m-1
        B[s]=A[i]
print(len(B)-1)
