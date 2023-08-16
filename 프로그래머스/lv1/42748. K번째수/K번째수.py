def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        a,b,c=commands[i][0], commands[i][1], commands[i][2]
        temp=array[a-1:b]
        temp.sort()
        answer.append(temp[c-1])
    return answer