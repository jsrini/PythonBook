import Queue
class Node:
  def __init__(self,index,data=None):
    self.data=data
    self.index=index
    self.edges=[]
    self.visited=False

  def addedge(self,node):
    if node not in self.edges:
      self.edges.append(node)

  def deleteedge(self,node):
    if node in self.edges:
      self.edges.remove(node)

  def isEdge(self,node):
    return node in self.edges
  
  def setVisited(self,val):
    self.visited=val
    
  def setData(self,data):
    self.data=data
    
  def printedges(self):
    E=[]
    for v in self.edges:
      E.append((self.index,v.index))
    print(E)

  def DepthFirstTraverse(self):
    if self.visited == True:
      return
    self.visited = True
    print(str(self.data))
    for adj in self.edges:
      adj.DepthFirstTraverse()
      
  def BreadthFirstTraverse(self, queue):
    for adj in self.edges:
      if adj.visited==False:
        adj.visited=True
        queue.enqueue(adj)
        
class Graph:
  def __init__(self,numvertices):
    self.nodes=[]
    for i in range(numvertices):
      self.nodes.append(Node(i))

  def setvertex(self,u,data):
    if u < len(self.nodes):
      self.nodes[u].data=data
    else:
      print('Incorrect vertex number')

  def addedge(self,u,v):
    if (u<len(self.nodes)) and (v<len(self.nodes)):
      if(self.nodes[u].isEdge(self.nodes[v])):
        print('Duplicate edge ('+str(u)+','+str(v)+')')
      else:
        self.nodes[u].addedge(self.nodes[v])
        self.nodes[v].addedge(self.nodes[u])
    else:
        print('Incorrect vertex number')
  
  def deleteedge(self,u,v):
    if (u<len(self.nodes)) and (v<len(self.nodes)):
        self.nodes[u].deleteedge(self.nodes[v])
        self.nodes[v].deleteedge(self.nodes[u])
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
      self.nodes[i].printedges()

  def DepthFirstTraverse(self):
    if len(self.nodes) > 0:
      self.nodes[0].DepthFirstTraverse()

  def DepthFirstTraverse2(self):
    for node in self.nodes:
      node.DepthFirstTraverse()
  
  def BreadthFirstTraverse(self):
    queue = Queue.Queue()
    for node in self.nodes:
      if node.visited==False:
        node.visited=True
        queue.enqueue(node)
        while queue.isEmpty()==False:
          curnode=queue.dequeue()
          print(str(curnode.data))
          curnode.BreadthFirstTraverse(queue)
          
      
