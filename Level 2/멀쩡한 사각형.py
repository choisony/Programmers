def gcd(w,h):
    if h ==0:
        return w
    else:
        return gcd(h,w%h)
    
    
def solution(w,h):
    if h>w:
        w,h = h,w
    g = gcd(w,h)
    
    return w*h-(w+h-g)
 
