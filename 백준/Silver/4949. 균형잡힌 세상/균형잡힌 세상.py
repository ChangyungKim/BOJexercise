import sys
line=sys.stdin.readline().rstrip()
while line!='.':
    stack=[]
    temp=True
    for i in range(len(line)):
        if line[i]=='(' or line[i]=='[':
            stack.append(line[i])
        elif line[i]==')':
            if not stack or stack[-1]=='[':
                temp=False
                break
            elif stack[-1]=='(':
                stack.pop()
        elif line[i]==']':
            if not stack or stack[-1]=='(':
                temp=False
                break
            elif stack[-1]=='[':
                stack.pop()
    if temp==True and len(stack)==0:
        print('yes')
    else:
        print('no')
    line=sys.stdin.readline().rstrip()
