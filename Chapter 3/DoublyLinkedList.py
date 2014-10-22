class Element:
    def __init__(self,data,prev=None,next=None):
        self.data=data
        self.prev=prev
        self.next=next
        
    def AddSuccessor(self, element):
        element.next = self.next
        if self.next!=None:
            self.next.prev=element
        self.next = element
        element.prev=self
        
    def AddPredecessor(self,element):
        element.next=self
        if self.prev!=None:
            self.prev.next=element
        element.prev=self.prev
        self.prev=element
        
    def DeleteElement(self):
        if self.prev!=None:
            self.prev.next=self.next
        if self.next!=None:
            self.next.prev=self.prev
        self.next=None
        self.prev=None
        return self.data
    
    
class DoublyLinkedList:
    def __init__(self,element=None):
        self.head = element
        self.tail = element
        
    def InsertTailElement(self, data):
        if self.tail!=None:
            self.tail.next=Element(data,self.tail)
            self.tail = self.tail.next
        else:
            self.head=Element(data)
            self.tail=self.head
        
    def InsertHeadElement(self, data):
        if self.head!=None:
            self.head.prev=Element(data,None,self.head)
            self.head = self.head.prev
        else:
            self.head=Element(data)
            self.tail=self.head
        
    def DeleteHeadElement(self):
        current=self.head
        if self.head!=None:
            self.head=current.next
            if self.head!=None:
                self.head.prev=None
            else:
                self.tail=None  
        if current!=None:
            current.next=None
            current.prev=None
            return current.data
        else:
            return None
    
    def DeleteTailElement(self):
        current=self.tail
        if self.tail!=None:
            self.tail=self.tail.prev
            if self.tail!=None:
                self.tail.next=None
            else:
                self.head=None
        if current!=None:
            current.next=None
            current.prev=None
            return current.data
        else:
            return None
            
    def PrintList(self):
        current=self.head
        while current != None:
            print('element: '+str(current.data))
            current=current.next
            
    def ProcessListElements(self, processfunction, otherprocessparams=None):
        current=self.head
        while current!=None:
            if otherprocessparams==None:
                processfunction(current)
            else:
                processfunction(current,otherprocessparams)
            current = current.next
	
