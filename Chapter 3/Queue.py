import LinkedList_Tail

class Queue:
    def __init__(self,data=None):
        self.elements=LinkedList_Tail.LinkedList()
        if data != None:
            self.elements.InsertTailElement(data)
    def enqueue(self,data):
        self.elements.InsertTailElement(data)
    def dequeue(self):
        return self.elements.DeleteHeadElement()
    def isEmpty(self):
        return self.elements.head==None
