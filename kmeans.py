"""
k means

input: 
	points = list of points, 2d, 
	k = number of clusters

output:
	list of centroids
	cluster assignments

process:
- randomly initialize k cluster centroids
- distance function, euclidean
A) for each point:
- calcualte distance between each point and each centroid, find the lowest distance one, then assign it
update the centroid locations:
B) for each centroid:
	find the average (x,y) of all points assigned to cluster 1, 
	set that as the new center
stop criteria:
	when relative movement 
	from r1 to r2: sum of centroid deltas. d1 -> d2 -> d3
	(d3/d2) / (d2/d1) > 0.99
"""

def kmeans(points, k):
	centroids = random.sample(points, k) # init k random centroids
	assignments = {}
	# initial assignments

	while stop_ratio < 0.001:
		prev_delta = delta
		assignments = assignstep()
		centroids, delta = updatecentroid()
		stop_ratio = delta/prev_delta

	return assigments, centroids

def assignstep(points, centroids):
	assignments = {}
	for x,y in points:
		mindist = sys.maxint
		bestcentroid = 0
		for i, c in enumerate(centroids):
			d = distance((x,y), c)
			if d < mindist:
				mindist = d
				bestcentroid = i
		if bestcentroid is in assignments:
			assignments[bestcentroid] += [(x,y)]
		else:
			assignments[bestcentroid] = [(x,y)]

	return assignments

def updatecentroid(assignments, centroids):
	for centroid in assignments:
		listofpoints = assignments[centroid]
		center = find_center(listofpoints)




def distance(a, b):
	return math.sqrt((a[1] - b[1])^2 + (a[0] - b[0])^2)

