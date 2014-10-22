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
        else:
            self.next=None
            return None
        return element.data
    
class LinkedList:
    def __init__(self,element=None):
        self.head = element
    def InsertTailElement(self, data):
        current=self.head
        if current == None:
            self.head=Element(data)
            return
        while current.next != None:
            current=current.next
        current.next=Element(data)
        
    def InsertHeadElement(self, data):
        el=Element(data)
        el.next=self.head
        self.head=el
        
    def DeleteHeadElement(self):
        current=self.head
        self.head=current.next
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
	
