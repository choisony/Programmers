https://school.programmers.co.kr/learn/courses/30/lessons/118667#

from collections import deque

def solution(queue1, queue2):
    answer = 0
    q1 = deque(queue1)
    q2 = deque(queue2)
    q1_sum = sum(q1)
    q2_sum = sum(q2)
    target = (q1_sum+q2_sum)/2

    while(q1 and q2):
        if q1_sum > target:
            temp = q1.popleft()
            q1_sum -= temp
            answer+=1
        elif q1_sum < target:
            temp = q2.popleft()
            q1.append(temp)
            q1_sum += temp
            answer+=1
        else:
            return answer
    
    else:
        return -1
