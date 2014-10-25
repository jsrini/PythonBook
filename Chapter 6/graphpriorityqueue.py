class minheap:
    def __init__(self,n):
        self.list=[]
        self.vertices=[-1]*n

    def insert(self,element):
        if self.vertices[element.vertex]==-1:
            #location of last element
            self.list.append(element)
            self.vertices[element.vertex]=len(self.list)-1
        self.reorderheap(element)
        
    def delete(self):
        if len(self.list) == 0:
          print('No element to delete')
          return
      
        retval = self.list[0]
        lastelt = self.list.pop()
        self.vertices[retval.vertex]=-1

        if lastelt==retval:
            return retval
        
        loc=0     
        done=False
        while done==False:
          lc=2*loc+1
          rc=2*loc+2
          maxindex = loc
          self.list[loc]=lastelt
          self.vertices[lastelt.vertex]=loc
          if lc < len(self.list):
            if self.list[lc].weight < lastelt.weight:
              maxindex=lc
          if rc < len(self.list):
            if self.list[rc].weight < self.list[maxindex].weight:
              maxindex=rc
          if maxindex != loc:
            self.list[loc]=self.list[maxindex]
            self.vertices[self.list[loc].vertex]=loc
            loc = maxindex
          else:
            return retval

    def reorderheap(self,element):
        loc = self.vertices[element.vertex]

        if self.list[loc].weight < element.weight:
            #no need to insert, current element has greater priority
            return
        done=False
        while done==False:
          if loc==0:
            self.list[loc]=element
            self.vertices[element.vertex]=loc
            return
          if self.list[loc//2].weight > element.weight:
            self.list[loc]=self.list[loc//2]
            self.vertices[self.list[loc].vertex]=loc
            loc = loc//2
          else:
            self.list[loc] = element
            self.vertices[element.vertex]=loc
            return
      
    def isEmpty(self):
        return len(self.list)==0
    
    def printheap(self):
        print("**********")
        for n in self.list:
          print(str(n.weight))
        print('---------')
