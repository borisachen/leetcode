x = [6,3,7,2,4,7,2]

def mergesort(x):
	if len(x) <= 1: return x
	mid = len(x)/2
	l = mergesort(x[0:mid])
	r = mergesort(x[mid:])
	res = merge(l, r)
	return res

def merge(x1, x2):
	if not x1: return x2
	if not x2: return x1
	res = []
	while x1 and x2:
		if x1[0] <= x2[0]:
			res.append(x1.pop(0))
		elif x2[0] <= x1[0]:
			res.append(x2.pop(0))
	if x1: res = res + x1
	if x2: res = res + x2
	return res


merge([2,4,7,8],[1,3,5,7])

mergesort(x)