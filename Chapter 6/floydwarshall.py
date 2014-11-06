import weightedgraph

def floyd_warshall(G):
    distances = [[float('inf') for i in range(G.numnodes())]
                 for j in range(G.numnodes())]
    
    for i in range(G.numnodes()):
        distances[i][i]=0
    predecessors = [[-1 for i in range(G.numnodes())]
                    for j in range(G.numnodes())]
    
    E = []
    for v in range(G.numnodes()):
        E.extend(G.getNode(v).getedges())

    for u, v, w in E:
        predecessors[u][v] = u
        distances[u][v] = w
    
    for k in range(G.numnodes()):
        for i in range(G.numnodes()):
            for j in range(G.numnodes()):
                newdist = distances[i][k]+distances[k][j]
                if newdist < distances[i][j]:
                    distances[i][j] = newdist
                    predecessors[i][j] = predecessors[k][j]

    for v in range(G.numnodes()):
        for u in range(G.numnodes()):
            if v == u:
                if predecessors[u][v] != -1:
                    print('There is a negative cycle in '
                          'the graph that includes vertex '+str(u))
                continue
            if predecessors[u][u] != -1:
                print('There is a negative cycle in '
                      'the path from '+ str(u) +
                      ' to ' + str(v))
                continue
            elif distances[u][v] == float('inf'):
                print('NO PATH from node '+str(u) +
                      ' to node '+ str(v))
                continue
            else:
                print('Shortest path (cost = '+
                      str(distances[u][v]) +
                      ') from node '+ str(u) +
                      ' to node '+ str(v)+': ')
            stack = [v]
            done = False
            currentnode = v

            while not done:
                currentnode=predecessors[u][currentnode]
                if currentnode != -1:
                    stack.append(currentnode)
                else:
                    done = True
            stack.reverse()
            print(stack)

        
            
