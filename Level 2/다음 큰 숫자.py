https://school.programmers.co.kr/learn/courses/30/lessons/12911

def solution(n):
    answer = 0
    temp = n+1
    while(str(bin(temp)).count('1') != str(bin(n)).count('1')):
        temp+=1
    return temp
