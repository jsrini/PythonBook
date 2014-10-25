import LinkedList

mylist=LinkedList.LinkedList()
mylist.InsertHeadElement(2)
mylist.InsertHeadElement(1)
mylist.InsertTailElement(3)
mylist.InsertTailElement(5)
mylist.InsertTailElement(6)
mylist.InsertTailElement(7)

def myownprint(element):
    print('element is: '+str(element.data))

def myListProcessor(element,params):
    if element.data == params[0]:
        #add a new element
        el = LinkedList.Element(params[1])
        element.AddSuccessor(el)
    if element.data==params[2]:
        element.DeleteSuccessor()

mylist.ProcessListElements(myownprint)
mylist.ProcessListElements(myListProcessor,[3,4,6])
mylist.PrintList()
