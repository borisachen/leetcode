121. Best Time to Buy and Sell Stock 

Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Example 1:
Input: [7, 1, 5, 3, 6, 4]
Output: 5

max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)
Example 2:
Input: [7, 6, 4, 3, 1]
Output: 0

In this case, no transaction is done, i.e. max profit = 0.

1. dp
keep track of smallestseen 
loop through, at each step, check prices[i] - smallestseen 

class Solution(object):
	def maxProfit(self, prices):
		"""
		:type prices: List[int]
		:rtype: int
		"""
		if not prices: return 0
		dp = [0]*len(prices)
		smallestseen = prices[0]
		for i in range(len(prices)):
			if prices[i] < smallestseen: smallestseen = prices[i]
			dp[i] = max(dp[i-1], prices[i] - smallestseen)
		return dp[-1]