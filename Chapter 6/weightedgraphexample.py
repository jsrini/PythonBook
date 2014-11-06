import weightedgraph
import kruskal

nodenumbers = {'John':0, 'Sally':1, 'George':2,
               'Phil':3, 'Rose':4, 'Alice':5}

G = weightedgraph.Graph(len(nodenumbers))
for node in nodenumbers:
  G.set_vertex(nodenumbers[node],node)

G.add_edge(nodenumbers['John'],nodenumbers['Sally'],1)
G.add_edge(nodenumbers['John'],nodenumbers['George'],2)
G.add_edge(nodenumbers['John'],nodenumbers['Rose'],3)
G.add_edge(nodenumbers['George'],nodenumbers['Sally'],4)
G.add_edge(nodenumbers['Phil'],nodenumbers['Sally'],5)
G.add_edge(nodenumbers['Rose'],nodenumbers['Alice'],6)

G.print_graph()

#print('Depth First Traversal:')
#G.DepthFirstTraverse()


#print('Depth First Traversal2:')
#G.DepthFirstTraverse2()

print('Breadth First Traversal:')
G.breadth_first_traverse()
#E=G.sortEdges()
#print(E)

MST=kruskal.Kruskal(G)
MST.print_graph()
