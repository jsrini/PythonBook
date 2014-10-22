import math

def grahamscan(points):
    if len(points) < 3:
        return points
    #first find lowermost and leftmost point
    print('Got points: '+str(points))
    minpt = 0
    for i in range(len(points)):
        if points[i][1]< points[minpt][1]:
            minpt=i
        elif points[i][1]==points[minpt][1]:
            if points[i][0] < points[minpt][0]:
                minpt=i

    refpt=points[minpt]
    print('minpt: '+ str(refpt))
    points.sort(key=lambda x: math.atan2(x[1]-refpt[1],x[0]-refpt[0]))

    print('SORTED points: '+str(points))
    convexhull=[refpt]
    for i in range(len(points)):
        if points[i]==refpt:
            continue
        if len(convexhull) >=2:
            if isLeft(convexhull[-2],convexhull[-1],points[i])>0:
                convexhull.append(points[i])
            else:
                while len(convexhull)>1 and isLeft(convexhull[-2],convexhull[-1],points[i])<=0:
                    convexhull.pop()
                convexhull.append(points[i])
        else:
            convexhull.append(points[i])

    return convexhull

        
def isLeft(a,b,c):
    return (c[1]-a[1])*(b[0]-a[0]) - (b[1]-a[1])*(c[0]-a[0])

    
