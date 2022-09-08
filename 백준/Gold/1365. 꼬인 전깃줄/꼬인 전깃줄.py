import sys
N=int(sys.stdin.readline().rstrip())
port1=list(map(int, sys.stdin.readline().rstrip().split()))
port2=[0]

def bin_search(arr,s,e,target):
    while s<=e:
        m=(s+e)//2
        if arr[m]<target:
            s=m+1
        else:
            e=m-1
    return s

for i in range(len(port1)):
    if port1[i]>port2[-1]:
        port2.append(port1[i])
    else:
        point=bin_search(port2,0,len(port2)-1,port1[i])
        port2[point]=port1[i]
leng=len(port2)-1
print(len(port1)-leng)