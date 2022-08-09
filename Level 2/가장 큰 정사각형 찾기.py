https://school.programmers.co.kr/learn/courses/30/lessons/12905
  
def solution(board):

    dp = [[0] * len(board[0]) for i in range(len(board))]
    for i in range(len(board)):
        for j in range(len(board[0])):
            if i==0:
                dp[i][j] = board[i][j]
            elif j==0:
                dp[i][j] = board[i][j]
            else:
                if board[i][j] ==1:
                    dp[i][j] = min(dp[i-1][j-1],dp[i][j-1],dp[i-1][j])+1
    m=0
    for i in dp:
        m = max(m,max(i)*max(i))

    return m
