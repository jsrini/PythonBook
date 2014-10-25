def swap(a,b):
    temp = a
    a = b
    b = temp

def algorithm2(list):
    for i in range(0,len(list)-1,1):
        for j in range(i+1,len(list),1):
            # Swap Ni with Nj if greater
            if list[i] > list[j]:
                swap(list[i],list[j])
    
