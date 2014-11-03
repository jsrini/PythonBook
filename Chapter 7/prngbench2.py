import matplotlib.pyplot as pyplot

def prngbench(prngobj):
    # Num bins in histogram
    bins = 50

    # Avg num points per bin
    ppbin = 1000

    # Num calls to rand()
    iterations = ppbin * bins
    
    data = [0]*iterations
    
    for i in range(iterations):
         data[i] = prngobj.random()

    # Generate histogram
    pyplot.hist(data,bins)
    pyplot.xlabel("Value")
    pyplot.ylabel("Frequency")
    pyplot.show()
