def solution(x):
    lst=[]
    temp=x
    leng=len(str(x))
    for i in range(leng):
        lst.append(x%10)
        x=x//10
    if temp%sum(lst)==0:
        answer=True
    else:
        answer=False
    return answer
        