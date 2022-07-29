def solution(rows, columns, queries):
    d = [[0]* columns for i in range(rows)]
    a=1
    for i in d:
        for j in range(columns):
            i[j] =a
            a+=1
    
    answer= []
    
    for i in queries:
        x1=i[0]-1
        y1=i[1]-1
        x2=i[2]-1
        y2=i[3]-1
        m=99999
        tmp = d[x1+1][y1]
        m = min(tmp,m)
        for i in range(y1,y2+1):
            d[x1][i], tmp = tmp, d[x1][i]
            m = min(tmp,m)
        for i in range(x1+1,x2+1):
            d[i][y2], tmp = tmp, d[i][y2]
            m = min(tmp,m)
        for i in range(y2-1,y1-1,-1):
            d[x2][i], tmp = tmp, d[x2][i]
            m = min(tmp,m)
        for i in range(x2-1,x1,-1):
            d[i][y1] ,tmp = tmp ,d[i][y1]
            m = min(tmp,m)
        
        answer.append(m)
    return answer
