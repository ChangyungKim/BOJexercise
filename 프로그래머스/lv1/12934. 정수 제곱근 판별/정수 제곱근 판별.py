def solution(n):
    answer = 0
    flag=0
    for i in range(1,n+1):
        if n==i*i:
            flag=1
            answer=(i+1)**2
            break
    if flag==0:
        answer=-1
    return answer