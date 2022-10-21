########### Brute Froce ###########
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

########### Stack ###########
def solution(prices):
    answer = [0]*len(prices)
    stack = [0]
    for i in range(1,len(prices)):
        if prices[i] > prices[i-1]:
            stack.append(i)
        else:
            while(len(stack)>0 and prices[i] < prices[stack[-1]]):
                idx = stack.pop()
                answer[idx] = i-idx
            stack.append(i)
    for i in stack:
        answer[i] = len(prices)-(i+1)
    return answer
