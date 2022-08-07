https://school.programmers.co.kr/learn/courses/30/lessons/12949#

def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        tp = []
        for j in range(len(arr2[0])):
            temp =0
            for x in range(len(arr1[0])):
                temp += arr1[i][x]*arr2[x][j]
            tp.append(temp)
        answer.append(tp)
                    
    return answer
