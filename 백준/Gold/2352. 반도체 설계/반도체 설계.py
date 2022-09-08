import sys
n=int(sys.stdin.readline().rstrip())
lst=list(map(int, sys.stdin.readline().rstrip().split()))
lst2=[0]
def bin_search(arr, s,e, target):
    while s<=e:
        m=(s+e)//2
        if arr[m]<target:
            s=m+1
        else:
            e=m-1
    return s

for i in range(len(lst)):
    if lst[i]>lst2[-1]:
        lst2.append(lst[i])
    else:
        point=bin_search(lst2,0,len(lst2)-1,lst[i])
        lst2[point]=lst[i]
print(len(lst2)-1)