class Ghost:
    
    def __init__(self,color,x,y):
        self._color = color
        self._x = x
        self._y = y
	

    def changeColor(self,color):
        self._color = color

    def printPosition(self):
        print("x: " + str(self._x) + " y: " + str(self._y)) 
    
    def moveUp(self):
        self._y += 1

