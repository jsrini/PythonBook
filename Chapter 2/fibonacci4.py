FibonacciList = [0, 1]

def Fibonacci(n):
    Fn = 0  # F(n)

    start = len(FibonacciList)
    
    for i in range(start,n+1):
        Fn = FibonacciList[i-1] + FibonacciList[i-2]
        FibonacciList.append(Fn)
         

    return FibonacciList[n]
