import WeightedGraph
import dijkstra
import prim

nodenumbers = {'N1':0, 'N2':1, 'N3':2, 'N4':3}

G=WeightedGraph.Graph(len(nodenumbers))
for node in nodenumbers:
  G.setvertex(nodenumbers[node],node)

G.addedge(nodenumbers['N1'],nodenumbers['N2'],2)
G.addedge(nodenumbers['N1'],nodenumbers['N4'],2)

G.addedge(nodenumbers['N2'],nodenumbers['N3'],2)

G.addedge(nodenumbers['N3'],nodenumbers['N4'],-4)


G.printGraph()

dijkstra.dijkstra(G,nodenumbers['N1'])

print('****')

MST=prim.prim(G,nodenumbers['N1'])
MST.printGraph()
