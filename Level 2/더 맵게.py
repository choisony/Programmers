import heapq

def solution(scoville, K):
    answer = 0
    h= []
    for i in scoville:
        heapq.heappush(h,i)
    while(len(h) >=2 and h[0] < K):
        first = heapq.heappop(h)
        second = heapq.heappop(h)
        tmp = first + second*2
        heapq.heappush(h,tmp)
        answer+=1
    if h[0] < K:
        answer=-1
    return answer
