def solution(n):
    answer=[]
    leng=len(str(n))
    for i in range(leng):
        num=n%10
        answer.append(num)
        n=n//10
    return answer