import sys
N=sys.stdin.readline().rstrip()
lst=list(N)
sum=0
for i in lst:
    sum+=int(i)
if '0' in lst and sum%3==0:
    lst.sort(reverse=True)
    print("".join(lst))
else:
    print(-1)


