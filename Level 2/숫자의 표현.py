https://school.programmers.co.kr/learn/courses/30/lessons/12924

def solution(n):
    answer= 0
    for i in range(n+1):
        temp = 0
        while(temp<=n and i!=0):
            temp +=i
            i-=1
            if temp>=n:
                break
        if temp==n:
            answer+=1
    return answer
