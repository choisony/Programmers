def solution(s, n):
    answer = ''

    for i in s:
        t = ord(i)
        if i==" ":
            answer+= " "

        elif 97<=t<=122:
            if t+n>122:
                t = t+n-122+97-1
                answer+=chr(t)
            else:
                answer+=chr(t+n)
                
        elif 65<=t<=90:
            if t+n>90:
                t = t+n-90+65-1
                answer+=chr(t)
            else:
                answer+=chr(t+n)
            
    return answer
