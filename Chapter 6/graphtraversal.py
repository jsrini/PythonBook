import Graph

def DepthFirstTraverse(node):
  if node.visited == True:
    return
  node.visited = True
  print(str(node.data))
  for adj in node.getAdjacentNodes():
    DepthFirstTraverse(adj)
