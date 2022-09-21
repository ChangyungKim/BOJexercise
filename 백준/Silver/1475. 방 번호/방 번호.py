import sys
N=(sys.stdin.readline().rstrip())
string=len(N)
lst=[]
counting=[]
N=int(N)
count=0
temp=0
for i in range(string):
    num=N%10
    lst.append(num)
    N=N//10
if (lst.count(6)+lst.count(9))%2==0:
    temp=(lst.count(6)+lst.count(9))//2
else:
    temp=(lst.count(6)+lst.count(9))//2+1
maximum=0
for i in range(len(lst)):
    if lst[i]!=6 and lst[i]!=9:
        maximum=max(maximum, lst.count(lst[i]))
print(max(maximum, temp))
