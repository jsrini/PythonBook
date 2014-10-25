import Graph

nodenumbers = {'John':0, 'Sally':1, 'George':2, 'Phil':3, 'Rose':4, 'Alice':5}

G=Graph.Graph(len(nodenumbers))
for node in nodenumbers:
  G.setvertex(nodenumbers[node],node)

G.addedge(nodenumbers['John'],nodenumbers['Sally'])
G.addedge(nodenumbers['John'],nodenumbers['George'])
G.addedge(nodenumbers['John'],nodenumbers['Rose'])
G.addedge(nodenumbers['George'],nodenumbers['Sally'])
G.addedge(nodenumbers['Phil'],nodenumbers['Sally'])
G.addedge(nodenumbers['Rose'],nodenumbers['Alice'])

G.printGraph()

#print('Depth First Traversal:')
#G.DepthFirstTraverse()


#print('Depth First Traversal2:')
#G.DepthFirstTraverse2()

print('Breadth First Traversal:')
G.BreadthFirstTraverse()
