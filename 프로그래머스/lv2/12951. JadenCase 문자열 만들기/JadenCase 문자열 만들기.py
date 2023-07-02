def solution(s):
    lst=s.split(' ')
    answer=[]
    for i in lst:
        i=i.capitalize()
        answer.append(i)
    return ' '.join(answer)