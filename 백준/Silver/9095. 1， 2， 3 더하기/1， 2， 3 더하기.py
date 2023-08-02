import sys
T=int(sys.stdin.readline().rstrip())
result=[]
lst=[0]*11
lst[1]=1
lst[2]=2
lst[3]=4
for i in range(T):
    n=int(sys.stdin.readline().rstrip())
    for j in range(4, n+1):
        lst[j]=lst[j-1]+lst[j-2]+lst[j-3]
    result.append(lst[n])
    
for j in range(len(result)):
    print(result[j])
               