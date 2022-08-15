https://school.programmers.co.kr/learn/courses/30/lessons/70129

def solution(s):
    answer = [0,0]
    while(s != "1"):
        st = ''
        for i in s:
            if i=='1':
                st += i
            if i=='0':
                answer[1]+=1
                
        s = str(bin(len(st))[2:])
        answer[0]+=1
    return answer
