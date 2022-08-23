https://school.programmers.co.kr/learn/courses/30/lessons/81302

from collections import deque
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(candidate,place):
    q = deque()
    
    q.append(candidate)
    visited = [[0]*5 for i in range(5)]
    cnt = 0
    fx = q[0][0]
    fy = q[0][1]
    
    while(q):
        x,y = q.popleft()
        visited[x][y] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if abs(fx-nx)+abs(fy-ny) <=2:
                if nx<0 or nx>=5 or ny<0 or ny>=5:
                    continue
                if visited[nx][ny] ==1:
                    continue
                if place[nx][ny] == "X":
                    continue
                if place[nx][ny] == "P":
                    return False
                q.append((nx,ny))
    return True
                
def solution(places):
    answer = []
    for place in places:
        flag = 1
        candidates = []
        for i in range(5):
            for j in range(5):
                if place[i][j] == "P":
                    candidates.append((i,j))
                    
        for candidate in candidates:
            if not bfs(candidate,place):
                flag = 0
                break
        
        answer.append(flag)
                
    return answer
