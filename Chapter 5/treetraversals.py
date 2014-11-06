import treenode

tree = treenode.Node(10)
n7 = treenode.Node(7)
n8 = treenode.Node(8)
n9 = treenode.Node(9)
n11 = treenode.Node(11)
n12 = treenode.Node(12)

tree.add_lchild(n8)
n8.add_lchild(n7)
n8.add_rchild(n9)
tree.add_rchild(n12)
n12.add_lchild(n11)

print('Pre-Order')
tree.pre_order()

print('In-Order')
tree.in_order()

print('Post-Order')
tree.post_order()

print('Breadth-First')
tree.breadth_first()
