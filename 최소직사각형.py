def solution(sizes):
    answer = 0
    w,h= 0,0
    for i in sizes:
        if i[1]>=i[0]:
            i[0],i[1] = i[1],i[0]
        w = max(i[0],w)
        h = max(i[1],h)
    answer= w*h
        
    return answer
