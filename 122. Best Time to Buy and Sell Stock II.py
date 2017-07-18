122. Best Time to Buy and Sell Stock II 

Difficulty: Easy

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). 
However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

1. dp


class Solution(object):
	def maxProfit(self, prices):
		"""
		:type prices: List[int]
		:rtype: int
		"""
		if not prices: return 0
		total = 0
		for i in range(len(prices)-1):
			if prices[i+1] > prices[i]:
				total += prices[i+1] - prices[i]
		return total