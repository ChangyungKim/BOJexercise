import sys
n=int(sys.stdin.readline().rstrip())
for _ in range(n):
    str=sys.stdin.readline().rstrip()
    cnt=0
    sum=0
    for i in range(len(str)):
        if str[i]=='O':
            cnt+=1
            sum+=cnt
        elif str[i]=='X':
            cnt=0
    print(sum)