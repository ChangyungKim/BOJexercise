import sys
S=list(sys.stdin.readline().rstrip())
T=list(sys.stdin.readline().rstrip())
cond=False
while T:
    if T[-1]=='A':
        T.pop()
    elif T[-1]=='B':
        T.pop()
        T.reverse()
    if S==T:
        cond=True
        break
if cond==True:
    print(1)
else:
    print(0)
