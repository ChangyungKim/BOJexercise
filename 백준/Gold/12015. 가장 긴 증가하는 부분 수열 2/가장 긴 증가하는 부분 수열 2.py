import sys

N=int(sys.stdin.readline().rstrip())
A=list(map(int, sys.stdin.readline().rstrip().split()))
B=[0]
num=0

def bin_search(arr, s,e,target):
    while s<=e:
        m=(s+e)//2
        if arr[m]<target:
            s=m+1
        else:
            e=m-1
    return s


for i in range(len(A)):
    if A[i]>B[-1]:
        B.append(A[i])
    else:
        num=bin_search(B,0,len(B)-1,A[i])
        B[num]=A[i]

print(len(B)-1)
