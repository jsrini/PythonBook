import random
import math

class sampleCDF:
    def __init__(self,CDF,min,max,bins):
        self.min = min
        self.max = max
        self.bins = bins
        self.binsize = (max-min)/self.bins

        # Discretize CDF
        self.discCDF = [0]*self.bins
        for i in range(self.bins):
            self.discCDF[i] = CDF(min+i*self.binsize)

        random.seed()

 
    def random(self):
        # Find x for this probability
        target = random.random()

        # Binary search
        minidx = 0
        maxidx = self.bins - 1
        pivotidx = (maxidx - minidx) // 2

        while pivotidx != minidx and pivotidx != maxidx:

            # Adjust indices for next iteration
            if self.discCDF[pivotidx] <= target:
                minidx = pivotidx
            else:
                maxidx = pivotidx

            pivotidx = minidx + (maxidx - minidx) // 2

        # Interpolate between the two closest x-values
        slope = (self.discCDF[maxidx]-self.discCDF[minidx])/self.binsize;
        dx = (target-self.discCDF[minidx])/slope;

        return dx + self.min + minidx*self.binsize
 
            
