https://school.programmers.co.kr/learn/courses/30/lessons/49993

def solution(skill, skill_trees):
    answer = 0
    d={}
    for i in range(len(skill)):
        d[skill[i]] = i
    temp = []
    for i in skill_trees:
        s = ''
        for j in i:
            if j in d.keys():
                s +=j
        temp.append(s)
    for i in temp:
        if i == skill[:len(i)]:
            answer+=1
    return answer
