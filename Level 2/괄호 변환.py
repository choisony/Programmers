https://school.programmers.co.kr/learn/courses/30/lessons/60058
  
def check(p):
    stack = []
    for i in p:
        if i =="(":
            stack.append(i)
        else:
            if not stack:
                return False
            stack.pop()
    if stack:
        return False
    else:
        return True
    
def devide(p):
    open_p = 0
    close_p = 0
    for i in range(len(p)):
        if p[i] =="(":
            open_p +=1
        if p[i] == ")":
            close_p +=1
        if open_p == close_p:
            u = p[:i+1]
            v = p[i+1:]
            return u,v
    

def solution(p):
    answer = ''
    if not p:
        return ""
    u,v = devide(p)
    
    if check(u):
        return u + solution(v)
    else:
        answer+="("
        answer+=solution(v)
        answer+=")"
        for i in u[1:-1]:
            if i=="(":
                answer+=")"
            else:
                answer+="("
        return answer
    
    return answer
