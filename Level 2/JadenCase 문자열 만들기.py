https://school.programmers.co.kr/learn/courses/30/lessons/12951?language=python3
  
  
def solution(s):
    answer = ''
    temp = True
    for i in s:
        if i==" ":
            temp =True
            answer+=i
        elif temp == True:
            answer+= i.upper()
            temp = False
        else:
            answer+=i.lower()
    return answer
