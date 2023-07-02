def solution(brown, yellow):
    answer = []
    sum=brown+yellow
    for i in range(1,sum):
        if sum%i==0:
            j=sum//i
            if j*2+(i-2)*2==brown:
                answer.append(j)
                answer.append(i)
                break
    return answer