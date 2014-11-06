import weightedgraph
import dijkstra
import prim

nodenumbers = {'N1':0, 'N2':1, 'N3':2, 'N4':3}

G=weightedgraph.Graph(len(nodenumbers))
for node in nodenumbers:
  G.set_vertex(nodenumbers[node],node)

G.add_edge(nodenumbers['N1'],nodenumbers['N2'],2)
G.add_edge(nodenumbers['N1'],nodenumbers['N4'],2)
G.add_edge(nodenumbers['N2'],nodenumbers['N3'],2)
G.add_edge(nodenumbers['N3'],nodenumbers['N4'],-4)

G.print_graph()

dijkstra.dijkstra(G,nodenumbers['N1'])

print('****')

MST=prim.prim(G,nodenumbers['N1'])
MST.print_graph()
