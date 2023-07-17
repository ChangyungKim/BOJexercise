import sys
a,b=map(int, sys.stdin.readline().rstrip().split())
mini=min(a,b)
for i in range(mini,-1,-1):
    if a%i==0 and b%i==0:
        num1=i
        break
print(num1)
print((a//num1)*(b//num1)*num1)