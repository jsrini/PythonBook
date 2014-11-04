def DnC_convexhull(points, srted=False):
    #sort the entire list only once
    if srted==False:
        points.sort()

    #end-recursion if num points <=3    
    if ((len(points)<=3) and (len(points)>0)):
        return clockwise(points)
    elif (len(points)==0):
        input('Error: empty points')
        return []

    #divide
    left = len(points)//2
    lefthull = DnC_convexhull(points[0:left],True)
    righthull = DnC_convexhull(points[left:],True)

    #merge
    return merge(lefthull,righthull)

#return clockwise ordering of points with respect to point with smallest x
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
    islft=is_left(points[minx],points[(minx+1)%3],points[(minx+2)%3])
    if  islft > 0:
        pts=[points[minx],points[(minx+2)%3],points[(minx+1)%3]]
    elif islft < 0:
        pts = [points[minx],points[(minx+1)%3],points[(minx+2)%3]]
    else:
        #points are collinear so only keep first and last
        pts=sorted(points)
        pts= [pts[0],pts[-1]]
    return pts


def is_left(a,b,c):
    return (c[1]-a[1])*(b[0]-a[0]) - (b[1]-a[1])*(c[0]-a[0])

#get directions of point to left of a (la) and point to right of a (ra)
def get_dir_la_ra(a,b,la,ra):
    dirla =  is_left(a,b,la)  
    dirra =  is_left(a,b,ra)
    return (dirla, dirra)

#check if a-b is a left tangent. la and ra are points to left and right of a
def check_left_tangent(a,b, la, ra):
    dirla, dirra = get_dir_la_ra(a,b,la,ra)
    if (dirra==0) and (dirla==0):
        input('degenerate left tangent: a: '+str(a)+' b: '+str(b)+' la: '+str(la)+' ra: '+str(ra))
        
    if (dirra>=0) and (dirla>=0):
        return True
    else:
        return False

#check if a-b is a right tangent. la and ra are points to left and right of a
def check_right_tangent(a,b,la,ra):
    dirla, dirra = get_dir_la_ra(a,b,la,ra)
    if (dirra==0) and (dirla==0):
        input('degenerate rightangent: a: '+str(a)+' b: '+str(b)+' la: '+str(la)+' ra: '+str(ra))
        
    if ((dirla<=0) and (dirra<=0)):
        return True
    else:
        return False

#given the left hull and right hull, find the lower tangent to connect the two hulls
def get_lower_tangent(lefthull, righthull,a,b):
    la = (a-1)%len(lefthull)
    ra = (a+1)%len(lefthull)
    lb = (b-1)%len(righthull)
    rb = (b+1)%len(righthull)

    istangent=False
    while istangent==False:
        count=0
        while check_left_tangent(lefthull[a],righthull[b],lefthull[la],lefthull[ra])== False:
            a=(a+1) % len(lefthull)
            la = (a-1)%len(lefthull)
            ra = (a+1)%len(lefthull)
            count=count+1
            if count==len(lefthull):
                print('get_lower_tangent: Infinite loop in left hull')
    
        count=0
        while check_left_tangent(lefthull[a],righthull[b],righthull[lb],righthull[rb])== False:
            b=(b-1) % len(righthull)
            lb = (b-1)%len(righthull)
            rb = (b+1)%len(righthull)
            count=count+1
            if count==len(righthull):
                print('get_lower_tangent: Infinite loop in right hull')
        
        if check_left_tangent(lefthull[a],righthull[b],lefthull[la],lefthull[ra]):
            return [a,b]

#given the left hull and right hull, find the upper tangent to connect the two hulls
def get_upper_tangent(lefthull, righthull,a,b):
    la = (a-1)%len(lefthull)
    ra = (a+1)%len(lefthull)
    lb = (b-1)%len(righthull)
    rb = (b+1)%len(righthull)

    istangent=False
    while istangent==False:
        count=0
        while check_right_tangent(lefthull[a],righthull[b],lefthull[la],lefthull[ra])== False:
            a=(a-1) % len(lefthull)
            la = (a-1)%len(lefthull)
            ra = (a+1)%len(lefthull)
            count=count+1
            if count==len(lefthull):
                print('get_upper_tangent: Infinite loop in left hull')

        count=0        
        while check_right_tangent(lefthull[a],righthull[b],righthull[lb],righthull[rb])== False:
            b=(b+1) % len(righthull)
            lb = (b-1)%len(righthull)
            rb = (b+1)%len(righthull)
            count=count+1
            if count==len(righthull):
                print('get uppertangent: Infinite loop in right hull')
        
        if check_right_tangent(lefthull[a],righthull[b],lefthull[la],lefthull[ra]):
            return [a,b]

def is_collinear (a,b,c):
    return is_left(a,b,c)==0

def find_leftright_most_points(hull):
    minindex=0
    maxindex=0
    for i in range(len(hull)):
        if hull[i][0] < hull[minindex][0]:
            minindex = i
        if hull[i][0] > hull[maxindex][0]:
            maxindex = i
    return (minindex, maxindex)


#merge algorithm
#starting from la, clockwise to ua, then add ub, work clockwise until lb
#deal with special cases (2 points, collinearity, etc.)
def merge(lefthull,righthull):

    if len(lefthull) == 2 and len(righthull) == 2:
        #merging two lines to form convex hull
        lefthull.sort(key= lambda x: (x[1],x[0]))
        righthull.sort(key= lambda x: (x[1],x[0]))

        la, lb =get_lower_tangent(lefthull,righthull,0,0)
        ua, ub = get_upper_tangent(lefthull,righthull,1,1)
    else:
        #assume lefthull and righthull are in clockwise order
        leftmin, leftmax = find_leftright_most_points(lefthull)

        rightmin, rightmax= find_leftright_most_points(righthull)

        a=leftmax
        b=rightmin
       
        la, lb = get_lower_tangent(lefthull,righthull,a,b)   
        ua, ub = get_upper_tangent(lefthull,righthull,a,b)
        
    #now that we got the tangents, construct the hull
    maxpts = len(lefthull)+len(righthull)
    convexhull = []

    #start from la, work clockwise until you reach ua
    i=la
    while i!=ua:
        #if we find collinear points discard middle collinear point in sequence
        if len(convexhull)>2 :
            if is_collinear(convexhull[-2],convexhull[-1],lefthull[i]):
                convexhull[-1]=lefthull[i]
            else:    
                convexhull.append(lefthull[i])
        else:
            convexhull.append(lefthull[i])
        i=(i+1)%len(lefthull)

    #now add ua to the list
    if len(convexhull)>2:
            if is_collinear(convexhull[-2],convexhull[-1],lefthull[ua]):
                convexhull[-1]=lefthull[ua]
            else:    
                convexhull.append(lefthull[ua])
    else:
        convexhull.append(lefthull[ua])

    #now starting from ub, work clockwise until you reach lb
    i=ub
    while i!=lb:
        if len(convexhull)>2 :
            if is_collinear(convexhull[-2],convexhull[-1],righthull[i]):
                convexhull[-1]=righthull[i]
            else:    
                convexhull.append(righthull[i])
        else:
            convexhull.append(righthull[i])
        i=(i+1)%len(righthull)

    #add lb
    if len(convexhull)>2:
            if is_collinear(convexhull[-2],convexhull[-1],righthull[lb]):
                convexhull[i]=righthull[lb]
            else:    
                convexhull.append(righthull[lb])
    else:
        convexhull.append(righthull[lb])

    #convex hull is ready
    return convexhull
        
        
        
    
    
    
