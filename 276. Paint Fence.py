276. Paint Fence

There is a fence with n posts, each post can be painted with one of the k colors.

You have to paint all the posts such that no more than two adjacent fence posts have the same color.

Return the total number of ways you can paint the fence.

Note:
n and k are non-negative integers.

-----------------------------------
Dynamic programming approach
if i-1 and i-2 are the same, then i has k-1 options.
- there are k ways for i-1 and i-2
- 3rd post: k*(k-1)
if different, then i has k options
- there are k^2 ways for i-1 and i-2
- 3rd post: k*(k-1)*k
3rd post: k*(k-1) + k*(k-1)*k = (k-1)*(k + k*k)
dp[0] = k
dp[1] = k
dp[i] = (k-1) * dp[i-1][i-2]

Since we ony need the previous 2 states, we can improve storage to O(1) by not keeping the ones prior to i-2
-----------------------------------

# Normal DP O(n) storage
def paint(n, k):
	dp = [0]*n
	dp[0] = k
	dp[1] = k*k
	if n < 2: return dp[n]
	for i in range(2, n):
		dp[i] = (k-1)*(dp[i-1] + dp[i-2])
	return dp[n-1]

paint(3,3)

# Now with better O(1) storage
def paint(n, k):
	dp = [0, k, k*k, 0]
	for i in range(2,n):
		dp[3] = (k-1) * (dp[2] + dp[1])
		dp[1], dp[2] = dp[2], dp[3]
	return dp[3]

paint(3,3)
