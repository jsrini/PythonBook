import math

    
def euler(x0,y0,xmax,dx,fxy):

    nmax = math.ceil(xmax // dx)
    yn = y0
    xn = x0

    for i in range(nmax):
        yn = dx*fxy(xn,yn) + yn
        xn += dx

    return yn
