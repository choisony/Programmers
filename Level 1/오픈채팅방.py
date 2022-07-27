def solution(record):
    d={}
    result = []
    for i in record:
        temp= i.split()
        if temp[0]=="Enter":
            result.append("님이 들어왔습니다.")
            d[temp[1]] = temp[2]
        elif temp[0] =="Leave":
            result.append("님이 나갔습니다.")
        elif temp[0]=="Change":
            d[temp[1]] = temp[2]
    
    idx = 0
    for i in record:
        temp = i.split()
        if temp[0]=="Enter":
            result[idx] = d[temp[1]]+ result[idx]
            idx+=1
        if temp[0] =="Leave":
            result[idx] = d[temp[1]]+ result[idx]
            idx+=1

        
    
    return result
