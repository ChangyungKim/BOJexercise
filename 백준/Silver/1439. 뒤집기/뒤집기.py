import sys
cnt=0
string=sys.stdin.readline().rstrip()
for i in range(len(string)-1):
    if string[0]=='0':
        if string[i]=='0' and string[i+1]=='1':
            cnt+=1
    else:
        if string[i]=='1' and string[i+1]=='0':
            cnt+=1
print(cnt)
        
