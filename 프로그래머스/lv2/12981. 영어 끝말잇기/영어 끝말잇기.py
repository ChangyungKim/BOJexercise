def solution(n, words):
    answer = []
    count=0
    for i in range(1,len(words)):
        if words[i-1][-1]!=words[i][0]:
            answer.append(i%n+1)
            answer.append(i//n+1)
            break
        if words[i] in words[:i]:
            answer.append(i%n+1)
            answer.append(i//n+1)
            break
    if len(answer)==0:
        answer=[0,0]
    return answer