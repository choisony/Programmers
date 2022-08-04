https://school.programmers.co.kr/learn/courses/30/lessons/12981
  
  
def solution(n, words):
    answer = []
    d= {}
    for i in range(len(words)):
        if i>0 and words[i][0] != words[i-1][-1]:
            answer.append(i%n+1)
            answer.append(i//n+1)
            break  
        if words[i] in d:
            answer.append(i%n+1)
            answer.append(i//n+1)
            break
        else:
            d[words[i]]= 1
            
    
    return answer if len(answer)>0 else [0,0]
