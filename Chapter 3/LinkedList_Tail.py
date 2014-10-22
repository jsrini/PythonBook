class Element:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
        
    def AddSuccessor(self, element):
        element.next = self.next
        self.next = element
        
    def DeleteSuccessor(self):
        element=self.next
        if element!=None:
            self.next=element.next
            element.next=None
        return element.data
    
class LinkedList:
    def __init__(self,element=None):
        self.head = element
        self.tail = element
        
    def InsertTailElement(self, data):
        current=self.tail
        if current == None:
            self.head=Element(data)
            self.tail=self.head
            return
        current.next=Element(data)
        self.tail = current.next
        
    def InsertHeadElement(self, data):
        el=Element(data)
        el.next=self.head
        self.head=el
        
    def DeleteHeadElement(self):
        current=self.head
        self.head=current.next
        if self.head == None:
            self.tail=None
        return current.data
    
    def DeleteTailElement(self):
        current=self.head
        if current==None:
            return None
        prev=None
        while current.next != None:
            prev=current
            current = current.next
        if prev != None:
            prev.next = None
            self.tail=prev
        return current.data
            
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
	
