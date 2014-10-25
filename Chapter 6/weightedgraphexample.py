import WeightedGraph
import kruskal

nodenumbers = {'John':0, 'Sally':1, 'George':2, 'Phil':3, 'Rose':4, 'Alice':5}

G=WeightedGraph.Graph(len(nodenumbers))
for node in nodenumbers:
  G.setvertex(nodenumbers[node],node)

G.addedge(nodenumbers['John'],nodenumbers['Sally'],1)
G.addedge(nodenumbers['John'],nodenumbers['George'],2)
G.addedge(nodenumbers['John'],nodenumbers['Rose'],3)
G.addedge(nodenumbers['George'],nodenumbers['Sally'],4)
G.addedge(nodenumbers['Phil'],nodenumbers['Sally'],5)
G.addedge(nodenumbers['Rose'],nodenumbers['Alice'],6)

G.printGraph()

#print('Depth First Traversal:')
#G.DepthFirstTraverse()


#print('Depth First Traversal2:')
#G.DepthFirstTraverse2()

print('Breadth First Traversal:')
G.BreadthFirstTraverse()
#E=G.sortEdges()
#print(E)

MST=kruskal.Kruskal(G)
MST.printGraph()
