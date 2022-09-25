def solution(s):
    s=s.lower()
    if s.count('p')==0 and s.count('y')==0:
        answer=True
    else:
        if s.count('p')==s.count('y'):
            answer=True
        else:
            answer=False
    return answer