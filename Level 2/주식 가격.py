def solution(prices):
    answer = []
    for i in range(0,len(prices)):
        ans = 0
        for j in range(i+1,len(prices)):
            if prices[j]<prices[i]:
                ans+=1
                break
            else:
                ans+=1
        answer.append(ans)
            
    return answer
