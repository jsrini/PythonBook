import graphpriorityqueue
import weightedgraph

class NodeData:
    def __init__(self,vertex,MSTVertex,weight):
        self.vertex = vertex
        self.MSTVertex = MSTVertex
        self.weight = weight

def prim(G,root):
    MST = weightedgraph.Graph(G.numnodes())
    inMST = [False]*G.numnodes()
    graphPQ = graphpriorityqueue.MinHeap(G.numnodes())
    rootnode = NodeData(root,root,0)
    graphPQ.insert(rootnode)
    MSTwt = 0
    
    while not graphPQ.isEmpty():
        element = graphPQ.delete()
        
        MST.set_vertex(element.vertex,
                       G.getNode(element.vertex).data)
                       
        inMST[element.vertex] = True
        
        if element.vertex != element.MSTVertex:
            MST.addedge(element.vertex,
                        element.MSTVertex,
                        element.weight)
                        
            MSTwt=MSTwt+element.weight
        adjlist=G.getNode(element.vertex).getedges()
        
        for MSTVertex, candidatevertex, wt in adjlist:
            if not inMST[candidatevertex]:
                newelt = NodeData(candidatevertex,
                                  MSTVertex,wt)
                graphPQ.insert(newelt)

    print('MST weight: '+str(MSTwt))
    return MST

