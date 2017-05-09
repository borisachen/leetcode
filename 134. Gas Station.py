134. Gas Station

There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). 
You begin the journey with an empty tank at one of the gas stations.

Return the starting gas stations index if you can travel around the circuit once, otherwise return -1.

Note:
The solution is guaranteed to be unique.


1. naive, 
try starting each i. at each step, fill the tank, see if you can get back to the ith station. 

2. observations
if total gas > cost, there must be a solution
if car starts at A and cannot reach B, nothing between A and B can reach B
iterate through the stations,
keep track of start, running tank, and total shortage so far (total = negative number)
at each step, update the tank,
if tank is negaitve, means we cant get here
	so move the start index up
	add the deficit up to total
	reset tank to 0

class Solution(object):
	def canCompleteCircuit(self, gas, cost):
		"""
		:type gas: List[int]
		:type cost: List[int]
		:rtype: int
		"""
		start = total = tank = 0 
		for i in range(len(gas)):
			tank += gas[i] - cost[i]
			if tank < 0:
				start = i + 1
				total += tank
				tank = 0
		return -1 if total + tank < 0 else start
