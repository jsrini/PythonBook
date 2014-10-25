import time
from collections import deque

L1=deque(1000*[0])
L2=deque(5000*[0])
L3=deque(10000*[0])
L4=deque(50000*[0])
L5=deque(100000*[0])
L6=deque(500000*[])

def timethelist(L,n):
    for i in range(5):
        starttime=time.clock()
        l = L.pop(n)
        stoptime=time.clock()
        elapsed=stoptime-starttime
        print(str(l)+' : '+ str(round(elapsed,7)))

timethelist(L1,500)
timethelist(L2,2500)
timethelist(L3,5000)
timethelist(L4,25000)
timethelist(L5,50000)
timethelist(L6,250000)

