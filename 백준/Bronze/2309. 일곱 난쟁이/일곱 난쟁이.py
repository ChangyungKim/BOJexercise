import sys
lst=[]
for i in range(9):
    lst.append(int(sys.stdin.readline().rstrip()))
overhead=sum(lst)-100
lst.sort()
for i in range(8):
    flag=0
    for j in range(i+1, 9):
        if lst[i]+lst[j]==overhead:
            tmp1=lst[i]
            tmp2=lst[j]
lst.remove(tmp1)
lst.remove(tmp2)
for i in lst:
    print(i)