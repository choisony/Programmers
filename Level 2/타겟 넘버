def dfs(idx,result):
    global answer
    if len(numlist)==idx:
        if result ==t:
            answer+=1
        return 
    else:
        dfs(idx+1,result + numlist[idx])
        dfs(idx+1,result - numlist[idx])

def solution(numbers, target):
    global numlist , t ,answer
    answer = 0
    numlist = numbers
    t = target
    
    dfs(0,0)
    return answer
