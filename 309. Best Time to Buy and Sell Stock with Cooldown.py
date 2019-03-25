309. Best Time to Buy and Sell Stock with Cooldown
Medium/1173/42

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit.
You may complete as many transactions as you like (ie, buy one and sell one
share of the stock multiple times) with the following restrictions:

You may not engage in multiple transactions at the same time (ie, you must
sell the stock before you buy again).
After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
Example:

prices = [1, 2, 3, 0, 2]
maxProfit = 3
transactions = [buy, sell, cooldown, buy, sell]

1. DP approach
3 possible transactions, keep 3 arrays

buy[i]  = max profit for any sequence ending with buy on day i-1
sell[i]
rest[i]

now define transition functions:

buy[i]  = max(rest[i-1] - price, buy[i-1]) # buy
sell[i] = max(buy[i-1] + price, sell[i-1]) # buy on i-1, sell today, profit = +price; sell i-1, do nothing today
rest[i] = max(sell[i-1], buy[i-1], rest[i-1])

note 1: buy[i] <= res[i].
thus, rest[i] = max(sell[i-1], rest[i-1])

note 2: rest[i] <= sell[i]
thus, rest[i] = sell[i-1]

substitute to get:
buy[i]  = max(sell[i-2] - price, buy[i-1])
sell[i] = max(buy[i-1] + price, sell[i-1])


class Solution(object):
	def maxProfit(self, prices):
		"""
		:type prices: List[int]
		:rtype: int
		"""
		if not prices: return 0
		n = len(prices)
		buy = -prices[0]
		sell = 0
		buy_prev = 0
		sell_prev = 0
		for price in prices:
			buy_prev = buy
			buy = max(sell_prev - price, buy_prev)
			sell_prev = sell
			sell = max(buy_prev + price, sell_prev)
		return sell
