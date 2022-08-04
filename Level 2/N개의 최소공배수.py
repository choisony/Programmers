https://school.programmers.co.kr/learn/courses/30/lessons/12953#
  
def gcd(a,b):
    while(b!=0):
        a,b = b,a%b
    return a

def solution(arr):
    gc = arr[0] #최소공배수
    gd = arr[0] #최대공약수
    for i in range(len(arr)):
        gc = gcd(gd,arr[i])
        gd *= arr[i] / gc
    return gd

    

