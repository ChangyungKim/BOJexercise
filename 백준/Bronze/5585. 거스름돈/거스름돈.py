import sys
N=int(sys.stdin.readline().rstrip())
coin=[500,100,50,10,5,1]
total=1000-N
num=0
for c in coin:
    num+=total//c
    total%=c
print(num)
