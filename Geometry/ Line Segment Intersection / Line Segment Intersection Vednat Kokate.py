class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

def onSegment(p, q, r):
	if ( (q.x <= max(p.x, r.x)) and (q.x >= min(p.x, r.x)) and		(q.y <= max(p.y, r.y)) and (q.y >= min(p.y, r.y))):		return True
	return False

def orientation(p, q, r):	
	val = (float(q.y - p.y) * (r.x - q.x)) - (float(q.x - p.x) * (r.y - q.y))
	if (val > 0):		return 1
	elif (val < 0):		return 2
	else:		return 0

def doIntersect(p1,q1,p2,q2):
	o1 = orientation(p1, q1, p2)
	o2 = orientation(p1, q1, q2)
	o3 = orientation(p2, q2, p1)
	o4 = orientation(p2, q2, q1)

	if ((o1 != o2) and (o3 != o4)):		return True

	if ((o1 == 0) and onSegment(p1, p2, q1)):		return True

	if ((o2 == 0) and onSegment(p1, q2, q1)):		return True

	if ((o3 == 0) and onSegment(p2, p1, q2)):		return True

	if ((o4 == 0) and onSegment(p2, q1, q2)):		return True

	return False






for _ in range(int(input())):
    x1,y1,x2,y2,x3,y3,x4,y4=map(int,input().split())
    p1 = Point(x1, y1)
    q1 = Point(x2, y2)
    p2 = Point(x3, y3)
    q2 = Point(x4, y4)
    if doIntersect(p1, q1, p2, q2):
	    print("YES")
    else:
	    print("NO")


