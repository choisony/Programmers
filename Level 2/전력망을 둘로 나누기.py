def solution(n, wires):
    answer = -1
    d= [[0]*(n+1) for i in range(n+1)]
    mini = n
    if n==2:
        return 0
    for k in range(0,len(wires)):
        w = wires[:k]+wires[k+1:]
        a= set()
        s = []
        s.append(w[0][0])
        s.append(w[0][1])
        a.add(w[0][0])
        a.add(w[0][1])
        while(s):
            top = s.pop()
            for i in w:
                if i[0]==top and i[1] not in a:
                    s.append(i[1])
                    a.add(i[1])
                elif i[1]==top and i[0] not in a:
                    s.append(i[0])
                    a.add(i[0])
        print(a)
        mini= min(mini,abs(n-len(a)-len(a)))
        
            
                
        
            
        
    return mini
