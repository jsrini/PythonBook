import treenode

tree=treenode.Node(10)
n7=treenode.Node(7)
n8=treenode.Node(8)
n9=treenode.Node(9)
n11=treenode.Node(11)
n12=treenode.Node(12)

tree.addLChild(n8)
n8.addLChild(n7)
n8.addRChild(n9)
tree.addRChild(n12)
n12.addLChild(n11)

print('Pre-Order')
tree.preorder()

print('In-Order')
tree.inorder()

print('Post-Order')
tree.postorder()

print('Breadth-First')
tree.breadthfirst()
