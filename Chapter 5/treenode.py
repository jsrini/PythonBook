import Queue
class Node:
    def __init__(self,key,parent=None):
        self.key=key
        self.data=None
        self.parent = parent
        self.lchild=None
        self.rchild=None

    def addLChild(self, node):
        self.lchild=node
        node.parent = self

    def addRChild(self,node):
        self.rchild=node
        node.parent=self

    def hasLChild(self):
        return self.lchild != None

    def hasRChild(self):
        return self.rchild!=None

    def isLeaf(self):
        return (self.lchild==None) and (self.rchild==None)

    def preorder(self):
      print(self.key)
      if self.hasLChild():
        self.lchild.preorder()
      if self.hasRChild():
        self.rchild.preorder()

    def inorder(self):
      if self.hasLChild():
        self.lchild.inorder()
      print(self.key)
      if self.hasRChild():
        self.rchild.inorder()
        
    def postorder(self):
      if self.hasLChild():
        self.lchild.postorder()
      if self.hasRChild():
        self.rchild.postorder()
      print(self.key)

    def breadthfirst(self):
      queue = Queue.Queue(self)
      while queue.isEmpty()==False:
        node=queue.dequeue()
        print(str(node.key))
        if node.hasLChild():
          queue.enqueue(node.lchild)
        if node.hasRChild():
          queue.enqueue(node.rchild)
      
