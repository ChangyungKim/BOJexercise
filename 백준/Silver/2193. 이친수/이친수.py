import sys
N=int(sys.stdin.readline().rstrip())
lst=[0,1,1]
for i in range(3,91):
    lst.append(lst[i-1]+lst[i-2])
print(lst[N])
