def solution(n):
    answer=0
    leng=len(str(n))
    for i in range(leng):
        answer+=n%10
        n=n//10
    return answer