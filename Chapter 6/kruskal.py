import WeightedGraph


def initializeSet(n):
  parent =[0]*n
  for i in range(n):
    parent[i]=-1
  return parent

def findRoot(S,n):
  root=n
  while S[root] >0:
    root = S[root]
    #print('root: '+str(root)+' S['+str(root)+']: '+str(S[root]))
  if(S[n]>0):
    S[n]=root
  return root

def union(S,root1,root2):
  if S[root1] < S[root2]:
    S[root2] = root1
  elif S[root2] < S[root1]:
    S[root1] = root2
  else:
    S[root1]=root2
    S[root2]=S[root2]-1
    

def Kruskal(G):
  setroots=initializeSet(G.numnodes())
  MST=WeightedGraph.Graph(G.numnodes())
  for i in range(G.numnodes()):
    MST.setvertex(i,G.getNode(i).data)
  E=G.sortEdges()
  MSTwt=0
  for i in range(len(E)):
    u, v, w = E[i]
    rootu=findRoot(setroots,u)
    rootv=findRoot(setroots,v)
    #print('root[u:'+str(u)+']: '+str(rootu)+' root[v:'+str(v)+']: '+str(rootv))
    if rootu != rootv:
      union(setroots,rootu,rootv)
      print('Adding edge: '+ str((u,v,w)))
      MST.addedge(u,v,w)
      MSTwt = MSTwt+w
  print('MST weight: '+str(MSTwt))
  return MST


  
    
