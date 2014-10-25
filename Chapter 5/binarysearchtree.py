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

class BinarySearchTree:
    def __init__(self):
        self.root=None

    def insertNode(self,node):
        current=self.root
        done=False
        while not done:
            if current!= None:
                if current.key>node.key:
                    if current.hasLChild():
                       current=current.lchild
                    else:
                        current.addLChild(node)
                        done=True
                elif current.key < node.key:
                    if current.hasRChild():
                        current=current.rchild
                    else:
                        current.addRChild(node)
                        done=True
                else:
                    print('Error. key match. Cannot insert')
                    return
            else:
                self.root=node
                done=True

    def searchNode(self,key):
      current=self.root
      path = []
      done = False
      while not done:
        if current!=None:
          path.append(current.key)
          if current.key == key:
            return path
          elif current.key > key:
            current=current.lchild
          else:
            current=current.rchild
        else:
          done = True
      return ['Not found']

    def setParentsChild(self,node,child):
      if node.parent!=None:
        if node.parent.lchild==node:
          node.parent.lchild=child
        else:
          node.parent.rchild=child
      else:
        self.root=child
      if child!=None:
        child.parent=node.parent

    def findRightmostLDescendant(self, node):
      rightmost=node.lchild
      while True:
        if rightmost.hasRChild():
          rightmost=rightmost.rchild
        else:
          return rightmost
    
    def deleteNode(self, key):
      current=self.root
      done = False
      while not done:
        if current!=None:
          if current.key == key:
            if current.isLeaf():
              self.setParentsChild(current,None)
            elif current.hasLChild() and current.hasRChild():
              #has two children
              #find right-most left child
              rightmost=self.findRightmostLDescendant(current)
              self.setParentsChild(rightmost,rightmost.lchild)
              self.setParentsChild(current,rightmost)
              rightmost.lchild=current.lchild
              rightmost.rchild=current.rchild
              return current
            elif current.hasLChild():
              self.setParentsChild(current,current.lchild)
            else:
              self.setParentsChild(current,current.rchild)
            current.lchild=None
            current.rchild=None
            current.parent=None
            return current
          elif current.key > key:
            current=current.lchild
          else:
            current=current.rchild
        else:
          return None

