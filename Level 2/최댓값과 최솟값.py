https://school.programmers.co.kr/learn/courses/30/lessons/12939

def solution(s):
    answer = ''
    d = s.split(' ')
    t= []
    for i in d:
        t.append(int(i))
    t.sort()
    print(t)
    answer=str(t[0])+" "+str(t[-1])
    return answer
