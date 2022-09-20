import sys
N=int(sys.stdin.readline().rstrip())
words=[]
count=0
for i in range(N):
    word=sys.stdin.readline().rstrip()
    for i in range(len(word)-1):
        if word[i]!=word[i+1] and word[i+1:].count(word[i])!=0:
            count+=1
            break
print(N-count)
