import weightedgraph
import graphpriorityqueue

class NodeData:
    def __init__(self,vertex,Svertex,weight):
        self.vertex=vertex
        self.Svertex=Svertex
        self.weight=weight
        
def dijkstra(G,s):
    span_tree=WeightedGraph.Graph(G.numnodes())
    in_span_tree = [False]*G.numnodes()
    distances = [float('inf')]*G.numnodes()
    distances[s] = 0
    predecessors = [-1]*G.numnodes()
    E = []
    GraphPQ = graphpriorityqueue.minheap(G.numnodes())
    for v in range(G.numnodes()):
        E.extend(G.getNode(v).getedges())

    source = NodeData(s,-1,0)
    GraphPQ.insert(source)

    while not GraphPQ.isEmpty():
        element = GraphPQ.delete()
        span_tree.setvertex(element.vertex,
                         G.getNode(element.vertex).data)
        in_span_tree[element.vertex] = True
        
        if element.Svertex != -1:
            span_tree.addedge(element.vertex,
                           element.Svertex,
                           element.weight)
        
        adjlist = G.getNode(element.vertex).getedges()

        for Svertex, candidatevertex, wt in adjlist:
            if in_span_tree[candidatevertex] == False:
                if distances[candidatevertex] >
                   (distances[Svertex] + wt):
                       
                    predecessors[candidatevertex] = Svertex
                    distances[candidatevertex] = distances[Svertex]+wt
                    
                    newelt = NodeData(candidatevertex,
                                      Svertex,
                                      distances[candidatevertex])
                    GraphPQ.insert(newelt)

    for v in range(G.numnodes()):
        if v == s:
            continue
        if predecessors[v]==-1 or
           distances[v]==float('inf'):
            print('NO PATH from node '+ str(s) +
                  ' to node '+ str(v))
            continue
        else:
            print('Shortest path (cost = '+ str(distances[v])+
                  ') from node '+str(s)+' to node '+str(v)+': ')
        stack = [v]
        done = False
        current_node = v

        while not done:
            current_node = predecessors[current_node]
            if current_node != -1:
                stack.append(current_node)
            else:
                done = True
        stack.reverse()
        print(stack)
