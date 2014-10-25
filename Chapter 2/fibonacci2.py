FibonacciList = [0,1]

def Fibonacci(n):

    if n <= 1:
            return n
    else:
        try:
            a = FibonacciList[n-2]
        except:
            a = Fibonacci(n-2)
            FibonacciList.append(a)

        try:
            b = FibonacciList[n-1]
        except:
            b = Fibonacci(n-1)
            FibonacciList.append(b)

        return a + b

