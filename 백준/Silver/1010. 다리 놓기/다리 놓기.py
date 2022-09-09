import math
import sys
T=int(sys.stdin.readline().rstrip())
result=[]
for i in range(T):
    N,M=map(int, sys.stdin.readline().rstrip().split())
    result.append(math.comb(M,N))
for i in range(T):
    print(result[i])