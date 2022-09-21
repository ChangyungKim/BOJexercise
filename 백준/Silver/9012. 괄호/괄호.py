import sys
T=int(sys.stdin.readline().rstrip())
for i in range(T):
    flag=0
    stack=[]
    lst=sys.stdin.readline().rstrip()
    for c in lst:
        if c=='(':
            stack.append(c)
        else:
            try:
                stack.pop()
            except:
                flag=1
                break
    if len(stack)==0 and flag==0:
        print('YES')
    else:
        print('NO')