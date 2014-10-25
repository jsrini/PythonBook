import graphpriorityqueue
import WeightedGraph

class NodeData:
    def __init__(self,vertex,Svertex,weight):
        self.vertex=vertex
        self.Svertex=Svertex
        self.weight=weight

def prim(G,root):
    MST=WeightedGraph.Graph(G.numnodes())
    inMST=[False]*G.numnodes()
    graphPQ=graphpriorityqueue.minheap(G.numnodes())
    rootnode=NodeData(root,root,0)
    graphPQ.insert(rootnode)
    MSTwt=0
    while graphPQ.isEmpty()==False:
        element=graphPQ.delete()
        MST.setvertex(element.vertex,G.getNode(element.vertex).data)
        inMST[element.vertex]=True
        if element.vertex != element.Svertex:
            MST.addedge(element.vertex,element.Svertex,element.weight)
            MSTwt=MSTwt+element.weight
        adjlist=G.getNode(element.vertex).getedges()
        for Svertex, candidatevertex, wt in adjlist:
            if inMST[candidatevertex] == False:
                newelt=NodeData(candidatevertex, Svertex,wt)
                graphPQ.insert(newelt)
    print('MST weight: '+str(MSTwt))
    return MST

