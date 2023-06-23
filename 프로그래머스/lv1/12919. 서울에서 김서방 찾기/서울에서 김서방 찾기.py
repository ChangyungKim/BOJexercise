def solution(seoul):
    answer=''
    for i in range(len(seoul)):
        if "Kim" ==seoul[i]:
            answer=str(i)
    return '김서방은 '+answer+'에 있다'