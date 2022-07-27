import heapq

def disk_controller(jobs):
    h = []
    index, now, answer = 1,0,0
    start = -1
    while index <= len(jobs):
        for j in jobs:
            if start < j[0] <= now:
                heapq.heappush(h,[j[1],j[0]])
        if h:
            job = heapq.heappop(h)
            start = now
            now += job[0]
            answer += now - job[1]
            index+=1
        else:
            now+=1

    return answer // len(jobs)

print(disk_controller([[0, 3], [1, 9], [2, 6]]))
