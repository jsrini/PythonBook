import time

L1=1000*[0]
L2=5000*[0]
L3=10000*[0]
L4=50000*[0]
L5=100000*[0]
L6=500000*[]

def timethelist(L):
    for i in range(5):
        starttime=time.clock()
        l = len(L)
        stoptime=time.clock()
        elapsed=stoptime-starttime
        print(str(l)+' : '+ str(round(elapsed,7)))

timethelist(L1)
timethelist(L2)
timethelist(L3)
timethelist(L4)
timethelist(L5)
timethelist(L6)

