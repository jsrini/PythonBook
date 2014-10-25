def swap(a,b):
    temp = a
    a = b
    b = temp

def algorithm3(list):
    for i in range(0,len(list)-1,1):
        minpos = i
        for j in range(i+1,len(list),1):
            # Swap index of Ni with Nj if greater
            if list[minpos] > list[j]:
                minpos = j

        # Do a single swap per i
        swap(list[i],list[minpos]

             
