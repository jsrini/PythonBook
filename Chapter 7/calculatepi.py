import random
import math

def calculate_pi(N):
    totalcount = 0
    circlecount = 0

    for i in range(N):
        x = random.random()
        y = random.random()

        r = math.sqrt(x**2 + y**2)

        if r <= 1:
            circlecount += 1
        totalcount += 1

    return circlecount / totalcount * 4

        
