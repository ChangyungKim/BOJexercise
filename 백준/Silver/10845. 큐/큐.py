from collections import deque
import sys
que=deque()
N=int(sys.stdin.readline().rstrip())
for i in range(N):
    line=sys.stdin.readline().rstrip()
    if ' ' in line:
        lst=line.split()
        que.append(int(lst[1]))
    else:
        if line=='pop':
            if not que:
                print(-1)
            else:
                print(que.popleft())
        elif line=='size':
            print(len(que))
        elif line=='empty':
            if not que:
                print(1)
            else:
                print(0)
        elif line=='front':
            if not que:
                print(-1)
            else:
                print(que[0])
        else:
            if not que:
                print(-1)
            else:
                print(que[len(que)-1])
