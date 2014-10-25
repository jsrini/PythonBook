class Node:
  def __init__(self,index,data=None):
    self.data=data
    self.index=index
    self.visited=False

  def setVisited(self,val):
    self.visited=val
    
  def setData(self,data):
    self.data=data

class Graph:
  def __init__(self,numvertices):
    self.nodes=[]
    self.matrix = [[0 for i in range(numvertices)]
                   for j in range(numvertices)]
    for i in range(numvertices):
      self.nodes.append(Node(i))

  def setvertex(self,u,data):
    if u < len(self.nodes):
      self.nodes[u].data=data
    else:
      print('Incorrect vertex number')

  def addedge(self, u, v):
    if (u<len(self.nodes)) and (v<len(self.nodes)):
      self.matrix[u][v]=1
      self.matrix[v][u]=1
    else:
        print('Incorrect vertex number')

  def deleteedge(self, u, v):
    if (u<len(self.nodes)) and (v<len(self.nodes)):
      self.matrix[u][v]=0
      self.matrix[v][u]=0
    else:
      print('Incorrect vertex number')

  def getNodeNumber(self,data):
    for i in range(len(self.nodes)):
      if self.nodes[i].data==data:
        return self.nodes[i].index
    return None

  def printGraph(self):
    for i in range(len(self.nodes)):
      print('Node number: '+str(i)+' data: '+str(self.nodes[i].data))
      adjlist=[]
      for j in range(len(self.nodes)):
        if self.matrix[i][j]==1:
          adjlist.append((i,j))
      print(adjlist)
