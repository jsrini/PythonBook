import Queue
class Node:
  def __init__(self,index,data=None):
    self.data=data
    self.index=index
    self.edges=[]
    self.weights={}
    self.visited=False

  def addedge(self,node,weight):
    if node not in self.edges:
      self.edges.append(node)
      self.weights[node]=weight

  def deleteedge(self,node):
    if node in self.edges:
      self.edges.remove(node)
      del self.weights[node]

  def isEdge(self,node):
    return node in self.edges
  
  def setVisited(self,val):
    self.visited=val
    
  def setData(self,data):
    self.data=data
    
  def printedges(self):
    E=[]
    for v in self.edges:
      E.append((self.index,v.index, self.weights[v]))
    print(E)

  def getedges(self):
    E=[]
    for v in self.edges:
      E.append((self.index,v.index, self.weights[v]))
    return(E)

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

  def addedge(self,u,v,w):
    if (u<len(self.nodes)) and (v<len(self.nodes)):
      if(self.nodes[u].isEdge(self.nodes[v])):
        print('Duplicate edge ('+str(u)+','+str(v)+')')
      else:
        self.nodes[u].addedge(self.nodes[v],w)
        self.nodes[v].addedge(self.nodes[u],w)
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

  def getNode(self,n):
    if n >=0 and n < len(self.nodes):
      return self.nodes[n]
    else:
      return None

  def printGraph(self):
    for i in range(len(self.nodes)):
      print('Node number: '+str(i)+' data: '+str(self.nodes[i].data))
      self.nodes[i].printedges()


  def DepthFirstTraverse(self):
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
          
  def sortEdges(self):
    E=[]
    for i in range(len(self.nodes)):
      E.extend(self.nodes[i].getedges())
    E.sort(key=lambda x: x[2])
    print(E)
    return(E)

  def numnodes(self):
    return len(self.nodes)
