def mergesort(list):
    N = len(list)
    
    # Base case
    if N <= 1:
        return list

    # Construct sublists
    L1 = list[0:N//2]
    L2 = list[N//2:N]

    # Sort each sublist
    mergesort(L1)
    mergesort(L2)

    # Merge the two lists...
    i1 = 0
    i2 = 0
    count = 0


    # Compare elements in sublist
    # and place in merged list
    while i1 < len(L1) and i2 < len(L2):
        if L1[i1] < L2[i2]:        
            list[count] = L1[i1]
            i1+=1
        else:
            list[count] = L2[i2]
            i2+=1
        count+=1

    # Place remaining elements in
    # merged list
    if i1 == len(L1):
        remainder = L2
        irem = i2
    else:
        remainder = L1
        irem = i1

    for i in range(irem,len(remainder)):
        list[count] = remainder[i]
        count+=1
    
