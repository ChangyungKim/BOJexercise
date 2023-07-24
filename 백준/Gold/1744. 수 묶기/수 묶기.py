import sys
N=int(sys.stdin.readline().rstrip())
minus=[]
plus=[]
sum=0
for i in range(N):
    temp=int(sys.stdin.readline().rstrip())
    if temp>1:
        plus.append(temp)
    elif temp<1:
        minus.append(temp)
    else:
        sum+=temp
minus.sort()
plus.sort(reverse=True)
if len(plus)%2==0:
    for i in range(0, len(plus), 2):
        sum+=plus[i]*plus[i+1]
else:
    for i in range(0, len(plus)-1, 2):
        sum+=plus[i]*plus[i+1]
    sum+=plus[len(plus)-1]

if len(minus)%2==0:
    for i in range(0, len(minus), 2):
        sum+=minus[i]*minus[i+1]
else:
    for i in range(0, len(minus)-1, 2):
        sum+=minus[i]*minus[i+1]
    sum+=minus[len(minus)-1]
print(sum)
