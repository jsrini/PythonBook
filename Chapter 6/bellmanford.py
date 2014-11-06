import weightedgraph

def bellman_ford(G,s):
    distances = [float('inf')]*G.numnodes()
    distances[s] = 0
    predecessors = [-1]*G.numnodes()
    E = []
    for v in range(G.numnodes()):
        E.extend(G.getNode(v).getedges())
    
    for iter in range(G.numnodes()-1):
        for u, v, w in E:
            if distances[v] > (distances[u] + w):
                predecessors[v]=u
                distances[v]=distances[u]+w
    for u,v,w in E:
        if distances[v] > (distances[u] + w):
                distances[v]=float('-inf')

    for v in range(G.numnodes()):
        if v==s:
            continue
        if predecessors[v] == -1 or
           distances[v] == float('-inf'):
            print('NO PATH from node '+ str(s) +
                  ' to node '+str(v))
            continue
        else:
            print('Shortest path (cost = '+
                  str(distances[v]) +
                  ') from node '+ str(s)+
                  ' to node '+str(v)+': ')
        stack = [v]
        done = False
        currentnode = v
        while not done:
            currentnode = predecessors[currentnode]
            if currentnode != -1:
                stack.append(currentnode)
            else:
                done = True
        stack.reverse()
        print(stack)