import Graph

nodenumbers = {'John':0, 'Sally':1, 'George':2, 'Phil':3, 'Rose':4, 'Alice':5}

G=Graph.Graph(len(nodenumbers))
for node in nodenumbers:
  G.set_node_data(nodenumbers[node],node)

G.add_edge(nodenumbers['John'],nodenumbers['Sally'])
G.add_edge(nodenumbers['John'],nodenumbers['George'])
G.add_edge(nodenumbers['John'],nodenumbers['Rose'])
G.add_edge(nodenumbers['George'],nodenumbers['Sally'])
G.add_edge(nodenumbers['Phil'],nodenumbers['Sally'])
G.add_edge(nodenumbers['Rose'],nodenumbers['Alice'])

G.print_graph()

#print('Depth First Traversal:')
#G.depth_first_traverse()


#print('Depth First Traversal2:')
#G.depth_first_traverse2()

print('Breadth First Traversal:')
G.breadth_first_traverse()
