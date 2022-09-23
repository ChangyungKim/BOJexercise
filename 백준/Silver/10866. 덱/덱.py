import sys
from collections import deque
N=int(sys.stdin.readline().rstrip())
que=deque()
for i in range(N):
    line=sys.stdin.readline().rstrip()
    if ' ' in line:
        if 'front' in line:
            a,b=line.split()
            que.appendleft(int(b))
        else:
            a,b=line.split()
            que.append(int(b))
    else:
        if '_' in line:
            if 'front' in line:
                if not que:
                    print(-1)
                else:
                    print(que.popleft())
            else:
                if not que:
                    print(-1)
                else:
                    print(que.pop())
        else:
            if line=='size':
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

