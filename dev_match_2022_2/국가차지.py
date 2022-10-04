maps = ["AABCA.QA", "AABC..QX", "BBBC.Y..", ".A...T.A", "....EE..", ".M.XXEXQ", "KL.TBBBQ"]

def solution(maps):

    answer = 0
    visited = [[False]*len(maps[0]) for _ in range(len(maps))]
    def dfs(x,y):
        dx=[0,0,1,-1]
        dy=[1,-1,0,0]

        if maps[x][y] in d:
            d[maps[x][y]]+=1
        else:
            d[maps[x][y]] = 1
        if maps[x][y] !=".":
            visited[x][y] =True
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx>=0 and nx<len(maps) and ny>=0 and ny<len(maps[0]) and visited[nx][ny]==False and maps[nx][ny]!=".":
                dfs(nx,ny)

    real_d={}
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if visited[i][j] == False and maps[i][j] !=".":
                d={}
                dfs(i,j)
                d= sorted(d.items(),reverse=True,key = lambda x: (x[1],ord(x[0])))
                for k in d:
                    if k[1]==d[0][1]:
                        real_d[k[0]] = real_d.get(k[0],0)+k[1]
                    else:
                        real_d[d[0][0]] = real_d.get(d[0][0])+ k[1]
    real_d = sorted(real_d.items(),reverse=True,key = lambda x: x[1])
    print(real_d)

    answer = real_d[0][1]
    return answer
print(solution(maps))
