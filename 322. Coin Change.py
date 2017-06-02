322. Coin Change

You are given coins of different denominations and a total amount of money amount. 
Write a function to compute the fewest number of coins that you need to make up that amount. 
If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:
coins = [1, 2, 5], amount = 11
return 3 (11 = 5 + 5 + 1)

Example 2:
coins = [2], amount = 3
return -1.

Note:
You may assume that you have an infinite number of each kind of coin.

1. backtracking

add coins (largest first) greedily
if we hit the goal, done
if we pass the goal, kill search

2. dp
dp[i] = fewest number of coins to get ammount i
then for each coin in coins, dp[i] = min(dp[i-coin]+1)

dp[25]
consinder:
dp[25-1]+1
dp[25-2]+1
dp[25-5]+1
take the min of these for dp[i]

class Solution(object):
	def coinChange(self, coins, amount):
		"""
		:type coins: List[int]
		:type amount: int
		:rtype: int
		"""
		if not coins: return -1
		if amount == 0: return 0
		dp = [0]*(amount+1)
		for i in range(1, amount+1):
			temp = []
			for c in coins:
				if i - c >= 0:
					if dp[i-c] == -1: temp.append(1)
					else: temp.append(dp[i-c]+1)
			if temp: 
				dp[i] = min(temp)
				if dp[i] == 0: dp[i] = -1
			else:
				dp[i] = -1
		print dp
		return dp[-1]

Solution().coinChange(coins = [1, 2, 5], amount = 11)
Solution().coinChange(coins = [2], amount = 3)
Solution().coinChange(coins = [186,419,83,408], amount = 6249)


class Solution(object):
	def coinChange(self, coins, amount):
		"""
		:type coins: List[int]
		:type amount: int
		:rtype: int
		"""
		MAX = float('inf')
		dp = [0] + [MAX]*amount
		for i in range(1, amount+1):
			dp[i] = min([dp[i - c] if i - c >= 0 else MAX for c in coins]) + 1
		return [dp[amount], -1][dp[amount] == MAX]

3. BFS
O(b^d) = O(len(coins)^amount)
O(|V| + |E|)

class Solution(object):
	def coinChange(self, coins, amount):
		"""
		:type coins: List[int]
		:type amount: int
		:rtype: int
		"""
		if amount == 0: return 0
		value1 = [0] # current values to explore
		value2 = [] # holds next levels of values to explore
		nc = 0
		visited = [False] * (amount + 1)
		visited[0] = True
		while value1: 
			nc += 1 # keeps track of current depth
			for v in value1: # 0 
				for coin in coins: # 1 2 5
					newval = v + coin # 1 2 5
					if newval == amount: return nc
					elif newval > amount: continue
					elif not visited[newval]:
						visited[newval] = True
						value2.append(newval)
			value1, value2 = value2, []
		return -1














