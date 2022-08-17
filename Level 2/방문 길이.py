https://school.programmers.co.kr/learn/courses/30/lessons/49994

def solution(dirs):
    answer = 0
    x=5
    y=5
    dic = {}
    
    for i in dirs:
        print(i)
        if i=="U":
            if y==10:
                continue
            elif y<10:
                if (x,y,x,y+1) not in dic and (x,y+1,x,y) not in dic:
                    answer+=1
                    dic[(x,y,x,y+1)] = 1
                    dic[(x,y+1,x,y)] = 1
                    y+=1
                else:
                    y+=1

        if i=="D":
            if y==0:
                continue
            elif y>0:
                if (x,y,x,y-1) not in dic and (x,y-1,x,y) not in dic:
                    answer+=1
                    dic[(x,y,x,y-1)] = 1
                    dic[(x,y-1,x,y)] = 1
                    y-=1
                else:
                    y-=1

        if i=="L":
            if x==0:
                continue
            elif x>0:
                if (x,y,x-1,y) not in dic and (x-1,y,x,y) not in dic:
                    answer+=1
                    dic[(x,y,x-1,y)] = 1
                    dic[(x-1,y,x,y)] = 1
                    x-=1
                else:
                    x-=1
        if i=="R":
            if x==10:
                continue
            elif x<10:
                if (x,y,x+1,y) not in dic and (x+1,y,x,y) not in dic:
                    answer+=1
                    dic[(x,y,x+1,y)] = 1
                    dic[(x+1,y,x,y)] = 1
                    x+=1
                else:
                    x+=1

    return answer
