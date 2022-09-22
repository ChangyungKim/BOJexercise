import sys
N=int(sys.stdin.readline().rstrip())
stack=[]
for i in range(N):
    lst=sys.stdin.readline().rstrip()
    if ' ' in lst:
        line=lst.split()
        stack.append(int(line[1]))
    else:
        if lst=='pop':
            if len(stack)==0:
                print(-1)
            else:
                print(stack[-1])
                stack.pop()
        elif lst=='size':
            print(len(stack))
        elif lst=='empty':
            if not stack:
                print(1)
            else:
                print(0)
        else:
            if not stack:
                print(-1)
            else:
                print(stack[-1])
