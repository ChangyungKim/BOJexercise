import sys
N=int(sys.stdin.readline().rstrip())
lst=[0]*300
score=[0]*300
for i in range(N):
    lst[i]=(int(sys.stdin.readline().rstrip()))
score[0]=lst[0]
score[1]=lst[0]+lst[1]
score[2]=max(lst[0]+lst[2], lst[1]+lst[2])
for i in range(3,N):
    score[i]=max(score[i-3]+lst[i-1]+lst[i], score[i-2]+lst[i])
print(score[N-1])
