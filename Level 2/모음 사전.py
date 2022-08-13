https://school.programmers.co.kr/learn/courses/30/lessons/84512

from itertools import product

def solution(word):
    answer = 0
    words = []
    for i in range(1,6):
        for j in product(["A","E","I","O","U"],repeat =i):
            words.append("".join(list(j)))
    words.sort()
    answer= words.index(word)+1
    
    return answer
