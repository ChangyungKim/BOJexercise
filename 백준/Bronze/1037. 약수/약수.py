import sys
N=int(sys.stdin.readline().rstrip())
lst=list(map(int, sys.stdin.readline().rstrip().split()))
lst.sort()
print(lst[0]*lst[-1])
