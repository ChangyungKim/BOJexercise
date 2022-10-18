import sys
a=sys.stdin.readline().rstrip()
b=sys.stdin.readline().rstrip()
length=len(b)
cnt=0
i=0
while i<len(a):
    if a[i]==b[0] and a[i:i+length]==b:
        cnt+=1
        i=i+length
    else:
        i+=1
print(cnt)
        