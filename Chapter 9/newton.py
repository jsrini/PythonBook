
def newton(x0,accuracy,maxiter,f,fp=0):
    x1 = 0.0
    
    for i in range(maxiter):

        try:
            x1 = x0 - f(x0)/fp(x0)
        except:
            dx = accuracy*x0
            x1 = x0 - f(x0) / ((f(x0) - f(x0-dx))/dx)

        if abs(x1-x0)/x0 < accuracy:
            print("Iterated " + str(i) + " times")
            print("Achieved req. tolerance")
            break

        x0 = x1

        if i == maxiter - 1:
            print("Max. iterations reached.")
            break

    return x1
