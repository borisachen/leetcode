360. Sort Transformed Array

Given a sorted array of integers nums and integer values a, b and c. Apply a quadratic function of the form f(x) = ax2 + bx + c to each element x in the array.

The returned array must be in sorted order.

Expected time complexity: O(n)

Example:
nums = [-4, -2, 2, 4], a = 1, b = 3, c = 5,

Result: [3, 9, 15, 33]

nums = [-4, -2, 2, 4], a = -1, b = 3, c = 5

Result: [-23, -5, 1, 7]

-----
Approach 1:
Compute f(x) for each x in nums, sort. 
Time O(nlogn)
Space O(n)

Notes:
This doesnt use the fact that:
- nums is sorted
- f(x) is quadratic

Approach 2:
Since f(x) is convex and quadratic, it has a unique minimum.
we can compute ax2+bx and then use binary search to find the minimum.
From there we can use two pointers searching outwards from the min.
Time O(n)
Space O(n)

Approach 3:
We actually dont care where the middle is.
It is easier to do the two pointer search from the outside inwards.
if a > 0, then we look for the bigger of the elements.
if a < 0, then we want the smaller.
-----

def sort_transformed_array2(nums,a,b,c):
	import operator
	n = len(nums)
	fx = [a*x*x + b*x + c for x in nums]
	lo = 0
	hi = n-1
	if a == 0:
		if b > 0: return fx
		elif b < 0: return fx[::-1]
		else: return [c]*n
	if a > 0: compare = operator.gt
	if a < 0: compare = operator.le
	res = []
	while lo <= hi:
		if compare(fx[lo], fx[hi]):
			res.append(fx[lo])
			lo += 1
		else:
			res.append(fx[hi])
			hi -= 1
	if a > 0: res = res[::-1]
	return res

sort_transformed_array2(nums = [-4, -2, 2, 4], a = 1, b = 3, c = 5)
sort_transformed_array2(nums = [-4, -2, 2, 4], a = -1, b = 3, c = 5)




def sort_transformed_array(nums,a,b,c):
	n = len(nums)
	ax2bx = [a*x*x + b*x for x in nums]
	def find_min(nums, lo, hi):
		if lo == hi: 
			return nums
		if lo == hi - 1:
			return lo if nums[lo] < nums[hi] else hi
		mid = (lo + hi) / 2
		if nums[mid] < nums[mid-1]: # search right
			return find_min(nums, mid+1, hi)
		else: # search left
			return find_min(nums, lo, mid-1)
	bot = find_min(ax2bx, 0, n)
	# Two pointers, searching outwards
	l = bot - 1
	r = bot + 1
	idx = [bot]
	while l >= 0 and r < n:
		if ax2bx[l] < ax2bx[r]:
			idx.append(l)
			l -= 1
		else:
			idx.append(r)
			r += 1
	if l >= 0:
		idx.extend(range(l,-1, -1))
	else:
		idx.extend(range(r, n))
	res = [ax2bx[i] + c for i in idx] 
	return res

sort_transformed_array(nums = [-4, -2, 2, 4], a = 1, b = 3, c = 5)

sort_transformed_array(nums = [-4, -2, 2, 4], a = -1, b = 3, c = 5)






