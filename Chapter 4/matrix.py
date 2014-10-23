import copy

class matrix():
    
    def __init__(self,X):

        if not isinstance(X,list):
            raise TypeError('Matrices require a list of lists')

        if not isinstance(X[0],list):
            raise TypeError('Matrices require a list of lists')

        columns = len(X[0])
        
        for i in X:
            if len(i) != columns:
                raise TypeError('The matrix is not well-formed')

        self.list = X

    def __getitem__(self,index):
        return self.list[index[0]][index[1]]

    def __setitem__(self,index,value):
        self.list[index[0]][index[1]] = value

    def rows(self):
        return len(self.list)

    def cols(self):
        return len(self.list[0])

    def __str__(self):
        stringRep = "";
        for i in range(self.rows()):
            stringRep += "[ "
            for j in range(self.cols()):
                stringRep += str(self[i,j]) + ' '
            stringRep += "]\n"               

        return stringRep    

    def __add__(self,X):
        if self.rows() != X.rows():
            raise TypeError('Dimension (row) mismatch')
        if self.cols() != X.cols():
            raise TypeError('Dimension (column) mismatch')

        result = copy.deepcopy(self)

        for i in range(self.rows()):
            for j in range(self.cols()):
                result[i,j] = result[i,j] + X[i,j]

        return result
                

    def __sub__(self,X):
        if self.rows() != X.rows():
            raise TypeError('Dimension (row) mismatch')
        if self.cols() != X.cols():
            raise TypeError('Dimension (column) mismatch')

        result = copy.deepcopy(self)

        for i in range(self.rows()):
            for j in range(self.cols()):
                result[i,j] = result[i,j] - X[i,j]

        return result

    
