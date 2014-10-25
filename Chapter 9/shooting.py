import math
   
def euler2o(x0,y0,yp0,xmax,dx,fxy):

    # Number of steps
    nmax = math.ceil((xmax - x0 - dx) // dx)

    # Start x at 3rd step since
    # we have y0, and compute y1
    xn = x0 + 2*dx

    # y(x-dx) for first iteration
    yn0 = y0

    # Use Euler to compute
    # y(x) for 1st iteration
    yn = dx*yp0+yn0
    
    #Precompute dx^2
    dx2 = dx**2

    for i in range(nmax):
        yn1 = dx2*fxy(xn,yn0,yn,dx)+2*yn-yn0
        xn += dx

        yn0 = yn
        yn=yn1

    return yn1


def shooting(yp0,x0,y0,xf,yf,dx,accuracy,maxiter,fxy):

    f0 = euler2o(x0,y0,yp0,xf,dx,fxy) - yf
    yp1 = -f0 / (yp0)

    for i in range(maxiter):
        f1 = euler2o(x0,y0,yp1,xf,dx,fxy) - yf
        fp = (f1-f0)/(yp1-yp0)
        yp0 = yp1
        yp1 = yp0  - f1/fp

 
        if abs(f0/yf) < accuracy:
            print("Iterated " + str(i) + " times")
            print("Achieved req. tolerance")
            break


        if i == maxiter - 1:
            print("Max. iterations reached.")
            break

        f0 = f1

    return yp1

    
