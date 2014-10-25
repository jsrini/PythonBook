import WeightedGraph
import graphpriorityqueue

class NodeData:
    def __init__(self,vertex,Svertex,weight):
        self.vertex=vertex
        self.Svertex=Svertex
        self.weight=weight
        
def dijkstra(G,s):
    SPTree=WeightedGraph.Graph(G.numnodes())
    inSPTree=[False]*G.numnodes()
    distances = [float('inf')]*G.numnodes()
    distances[s]=0
    predecessors = [-1]*G.numnodes()
    E=[]
    GraphPQ = graphpriorityqueue.minheap(G.numnodes())
    for v in range(G.numnodes()):
        E.extend(G.getNode(v).getedges())

    source = NodeData(s,-1,0)
    GraphPQ.insert(source)
    while GraphPQ.isEmpty() == False:
        element=GraphPQ.delete()
        SPTree.setvertex(element.vertex,G.getNode(element.vertex).data)
        inSPTree[element.vertex]=True
        if element.vertex != -1:
            SPTree.addedge(element.vertex,element.Svertex,element.weight)
        adjlist=G.getNode(element.vertex).getedges()
        for Svertex, candidatevertex, wt in adjlist:
            if inSPTree[candidatevertex] == False:
                if distances[candidatevertex] > (distances[Svertex] + wt):
                    predecessors[candidatevertex]=Svertex
                    distances[candidatevertex]=distances[Svertex]+wt
                    newelt=NodeData(candidatevertex, Svertex,distances[candidatevertex])
                    GraphPQ.insert(newelt)

    for v in range(G.numnodes()):
        if v==s:
            continue
        if predecessors[v]==-1 or distances[v]==float('-inf'):
            print('NO PATH from node '+str(s)+' to node '+str(v))
            continue
        else:
            print('Shortest path (cost = '+str(distances[v])+') from node '+str(s)+' to node '+str(v)+': ')
        stack = [v]
        done=False
        currentnode = v
        while not done:
            currentnode=predecessors[currentnode]
            if currentnode != -1:
                stack.append(currentnode)
            else:
                done=True
        stack.reverse()
        print(stack)
