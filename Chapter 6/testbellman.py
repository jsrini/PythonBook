import WeightedGraph
import bellmanford

nodenumbers = {'N1':0, 'N2':1, 'N3':2, 'N4':3, 'N5':4, 'N6':5, 'N7':6, 'N8':7}

G=WeightedGraph.Graph(len(nodenumbers))
for node in nodenumbers:
  G.setvertex(nodenumbers[node],node)

G.addedge(nodenumbers['N1'],nodenumbers['N2'],3)
G.addedge(nodenumbers['N1'],nodenumbers['N4'],2)
G.addedge(nodenumbers['N1'],nodenumbers['N3'],3)

G.addedge(nodenumbers['N2'],nodenumbers['N4'],9)
G.addedge(nodenumbers['N2'],nodenumbers['N5'],4)
G.addedge(nodenumbers['N2'],nodenumbers['N7'],2)

G.addedge(nodenumbers['N3'],nodenumbers['N4'],4)
G.addedge(nodenumbers['N3'],nodenumbers['N5'],1)
G.addedge(nodenumbers['N3'],nodenumbers['N7'],6)
G.addedge(nodenumbers['N3'],nodenumbers['N8'],-6)

G.addedge(nodenumbers['N4'],nodenumbers['N6'],1)

G.addedge(nodenumbers['N5'],nodenumbers['N7'],7)


G.printGraph()

bellmanford.bellmanford(G,nodenumbers['N1'])
