class Line:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        if a[0]!=b[0]:
            self.m = (a[1]-b[1])/(a[0]-b[0])
            self.C = (a[1]*b[0]-b[1]*a[0])/(a[0]-b[0])
        else:
            self.m=float('inf')
            self.X = a[0]

    def isInLine(a):
        if self.m != float('inf'):
            if a[1] == self.m*a[0]+self.C:
                return True
            else:
                return False
        else:
            if a[0]==self.X:
                return True
            else:
                return False
            
