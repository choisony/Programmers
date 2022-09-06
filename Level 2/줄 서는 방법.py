from itertools import combinations
def solution(n, k):
    answer = []
    d = [[i] for i in range(1,n+1)]
    t = list(combinations(d,3))
    print(t)
        
    return answer
