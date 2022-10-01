import sys
N=int(sys.stdin.readline().rstrip())
dict={}
for i in range(N):
    title=sys.stdin.readline().rstrip()
    if title in dict:
        dict[title]+=1
    else:
        dict[title]=1
lst=[k for k,v in dict.items() if max(dict.values())==v]
lst.sort()
print(lst[0])
