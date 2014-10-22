def DnC_convexhull(points, srted=False):
    if srted==False:
        points.sort()

    print('DnC_convexhull: got points ' + str(points))
    
    if ((len(points)<=3) and (len(points)>0)):
        return clockwise(points)
    elif (len(points)==0):
        input('Error: empty points')
        return []
    
    left = len(points)//2
    #print('left='+str(left))
    #input('Enter val: ')
    
    print('about to recurse on left side'+str(points[0:left]))
    lefthull = DnC_convexhull(points[0:left],True)
    print('got lefthull: '+str(lefthull))

    print('about to recurse on right side'+str(points[left:]))
    righthull = DnC_convexhull(points[left:],True)
    print('got righthull: '+str(righthull))

    print('going to merge')
    return merge(lefthull,righthull)

def clockwise(points):
    if len(points)==1:
        return points
    i=0
    minx = 0
    for i in range(len(points)):
        if points[i][0] < points[minx][0]:
            minx=i

    if len(points)==2:
        return [points[minx],points[(minx+1)%2]]

    #points = 3
    islft=isLeft(points[minx],points[(minx+1)%3],points[(minx+2)%3])
    if  islft > 0:
        pts=[points[minx],points[(minx+2)%3],points[(minx+1)%3]]
    elif islft < 0:
        pts = [points[minx],points[(minx+1)%3],points[(minx+2)%3]]
    else:
        #points are collinear so only keep first and last
        pts=sorted(points)
        pts= [pts[0],pts[-1]]
    return pts


def isLeft(a,b,c):
    return (c[1]-a[1])*(b[0]-a[0]) - (b[1]-a[1])*(c[0]-a[0])

def getdirlara(a,b,la,ra):
    dirla =  isLeft(a,b,la)  
    dirra =  isLeft(a,b,ra)
    return (dirla, dirra)

def checklefttangent(a,b, la, ra):
    dirla, dirra = getdirlara(a,b,la,ra)
    if (dirra==0) and (dirla==0):
        input('degenerate left tangent: a: '+str(a)+' b: '+str(b)+' la: '+str(la)+' ra: '+str(ra))
        
    if (dirra>=0) and (dirla>=0):
        return True
    else:
        return False


def checkrighttangent(a,b,la,ra):
    dirla, dirra = getdirlara(a,b,la,ra)
    if (dirra==0) and (dirla==0):
        input('degenerate rightangent: a: '+str(a)+' b: '+str(b)+' la: '+str(la)+' ra: '+str(ra))
        
    if ((dirla<=0) and (dirra<=0)):
        return True
    else:
        return False

def getlowertangent(lefthull, righthull,a,b):
    #lower tangent
    la = (a-1)%len(lefthull)
    ra = (a+1)%len(lefthull)
    lb = (b-1)%len(righthull)
    rb = (b+1)%len(righthull)

    istangent=False
    while istangent==False:
        count=0
        while checklefttangent(lefthull[a],righthull[b],lefthull[la],lefthull[ra])== False:
            a=(a+1) % len(lefthull)
            la = (a-1)%len(lefthull)
            ra = (a+1)%len(lefthull)
            count=count+1
            if count==len(lefthull):
                print('getlowertangent: Infinite loop in left hull')
    
        count=0
        while checklefttangent(lefthull[a],righthull[b],righthull[lb],righthull[rb])== False:
            b=(b-1) % len(righthull)
            lb = (b-1)%len(righthull)
            rb = (b+1)%len(righthull)
            count=count+1
            if count==len(righthull):
                print('getlowertangent: Infinite loop in right hull')
        
        if checklefttangent(lefthull[a],righthull[b],lefthull[la],lefthull[ra]):
            return [a,b]

def getuppertangent(lefthull, righthull,a,b):
    #lower tangent
    la = (a-1)%len(lefthull)
    ra = (a+1)%len(lefthull)
    lb = (b-1)%len(righthull)
    rb = (b+1)%len(righthull)

    istangent=False
    while istangent==False:
        count=0
        while checkrighttangent(lefthull[a],righthull[b],lefthull[la],lefthull[ra])== False:
            a=(a-1) % len(lefthull)
            la = (a-1)%len(lefthull)
            ra = (a+1)%len(lefthull)
            count=count+1
            if count==len(lefthull):
                print('getuppertangent: Infinite loop in left hull')

        count=0        
        while checkrighttangent(lefthull[a],righthull[b],righthull[lb],righthull[rb])== False:
            b=(b+1) % len(righthull)
            lb = (b-1)%len(righthull)
            rb = (b+1)%len(righthull)
            count=count+1
            if count==len(righthull):
                print('get uppertangent: Infinite loop in right hull')
        
        if checkrighttangent(lefthull[a],righthull[b],lefthull[la],lefthull[ra]):
            return [a,b]

           
def merge(lefthull,righthull):
    print('merge: got lefthull: '+str(lefthull))
    print('merge: got righthull: '+str(righthull))

    if len(lefthull) == 2 and len(righthull) == 2:
        lefthull.sort(key= lambda x: (x[1],x[0]))
        righthull.sort(key= lambda x: (x[1],x[0]))

        print('merge: before getting lower tangent of two lines')
        la, lb =getlowertangent(lefthull,righthull,0,0)
        print('merge: after lower tangent. la: '+str(lefthull[la])+' lb: '+str(righthull[lb]))
        ua, ub = getuppertangent(lefthull,righthull,1,1)
        print('merge: after upper tangent. ua: '+str(lefthull[ua])+' ub: '+str(righthull[ub]))
    else:
        #assume lefthull and righthull are in clockwise order
        leftmin=0
        leftmax=0
        for i in range(len(lefthull)):
            if lefthull[i][0] < lefthull[leftmin][0]:
                leftmin = i
            if lefthull[i][0] > lefthull[leftmax][0]:
                leftmax = i

        rightmin=0
        rightmax=0
        for i in range(len(righthull)):
            if righthull[i][0] < righthull[rightmin][0]:
                rightmin = i
            if righthull[i][0] > righthull[rightmax][0]:
                rightmax = i

        a=leftmax
        b=rightmin

        print('leftmin: '+str(lefthull[leftmin])+' leftmax: '+str(lefthull[leftmax])+' rightmin: '+str(righthull[rightmin])+' rightmax: '+str(righthull[rightmax]))
        print('merge: before getting lower tangent')
        la, lb =getlowertangent(lefthull,righthull,a,b)
        print('merge: after lower tangent. la: '+str(lefthull[la])+' lb: '+str(righthull[lb]))
        ua, ub = getuppertangent(lefthull,righthull,a,b)
        print('merge: after upper tangent. ua: '+str(lefthull[ua])+' ub: '+str(righthull[ub]))

    maxpts = len(lefthull)+len(righthull)
    convexhull = []
    
    i=la
    while i!=ua:
        if len(convexhull)>2 :
            if isLeft(convexhull[-2],convexhull[-1],lefthull[i])==0:
                convexhull[-1]=lefthull[i]
            else:    
                convexhull.append(lefthull[i])
        else:
            convexhull.append(lefthull[i])
        i=(i+1)%len(lefthull)
    if len(convexhull)>2:
            if isLeft(convexhull[-2],convexhull[-1],lefthull[ua])==0:
                convexhull[-1]=lefthull[ua]
            else:    
                convexhull.append(lefthull[ua])
    else:
        convexhull.append(lefthull[ua])

    i=ub
    while i!=lb:
        if len(convexhull)>2 :
            if isLeft(convexhull[-2],convexhull[-1],righthull[i])==0:
                convexhull[-1]=righthull[i]
            else:    
                convexhull.append(righthull[i])
        else:
            convexhull.append(righthull[i])
        i=(i+1)%len(righthull)
    if len(convexhull)>2:
            if isLeft(convexhull[-2],convexhull[-1],righthull[lb])==0:
                convexhull[i]=righthull[lb]
            else:    
                convexhull.append(righthull[lb])
    else:
        convexhull.append(righthull[lb])
    
    print('merge.  constructed convex hull.  '+str(convexhull))
    return convexhull
        
        
        
    
    
    
