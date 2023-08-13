from collections import deque

def solution(maps):
    n=len(maps)
    m=len(maps[0])
    q=deque()
    q.append((0,0))
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    while q:
        (x,y)=q.popleft()
        for k in range(4):
            cx=x+dx[k]
            cy=y+dy[k]
            if cx<0 or cy<0 or cx>=n or cy>=m or maps[cx][cy]==0:
                continue
            if maps[cx][cy]==1:
                maps[cx][cy]=maps[x][y]+1
                q.append((cx,cy))
                
    answer = maps[n-1][m-1]
    if answer==1:
        return -1
    else:           
        return answer