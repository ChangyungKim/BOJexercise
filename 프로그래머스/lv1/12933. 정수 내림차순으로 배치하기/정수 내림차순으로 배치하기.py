def solution(n):
    lst=[]
    leng=len(str(n))
    answer=''
    for i in range(leng):
        lst.append(str(n%10))
        n=n//10
    lst.sort(reverse=True)
    for i in range(leng):
        answer=answer+lst[i]
    answer=int(answer)
    return answer