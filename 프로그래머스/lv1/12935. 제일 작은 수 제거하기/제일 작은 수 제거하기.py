def solution(arr):
    answer=arr
    answer.remove(min(answer))
    if len(arr)==0:
        answer=[-1]
    return answer
        