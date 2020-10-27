1027. Longest Arithmetic Subsequence
Medium/910/47

Given an array A of integers, return the length of the longest arithmetic subsequence in A.

Recall that a subsequence of A is a list A[i_1], A[i_2], ..., A[i_k] with 0 <= i_1 < i_2 < ... < i_k <= A.length - 1, 
and that a sequence B is arithmetic if B[i+1] - B[i] are all the same value (for 0 <= i < B.length - 1). 

Example 1:

Input: A = [3,6,9,12]
Output: 4
Explanation: 
The whole array is an arithmetic sequence with steps of length = 3.


Example 2:

Input: A = [9,4,7,2,10]
Output: 3
Explanation: 
The longest arithmetic subsequence is [4,7,10].


Example 3:

Input: A = [20,1,15,3,10,5,8]
Output: 4
Explanation: 
The longest arithmetic subsequence is [20,15,10,5].
 

Constraints:

2 <= A.length <= 1000
0 <= A[i] <= 500

"""
The main idea is to maintain a map of differences seen at each index.

We iteratively build the map for a new index i, by considering all elements to the left one-by-one.
For each pair of indices (i,j) and difference d = A[i]-A[j] considered, we check if there was an existing chain at the index j with difference d already.

If yes, we can then extend the existing chain length by 1.
Else, if not, then we can start a new chain of length 2 with this new difference d and (A[j], A[i]) as its elements.
At the end, we can then return the maximum chain length that we have seen so far.

Time Complexity: O(n^2)
Space Complexity: O(n^2)
"""
class Solution {
    public int longestArithSeqLength(int[] A) {
        if (A.length <= 1) return A.length;
       
        int longest = 0;
        
        # Declare a dp array that is an array of hashmaps.
        # The map for each index maintains an element of the form-
        #   (difference, length of max chain ending at that index with that difference).        
        HashMap<Integer, Integer>[] dp = new HashMap[A.length];
        
        for (int i = 0; i < A.length; ++i) {
            # Initialize the map.
            dp[i] = new HashMap<Integer, Integer>();
        }
        
        for (int i = 1; i < A.length; ++i) {
            int x = A[i];
            # Iterate over values to the left of i.
            for (int j = 0; j < i; ++j) {
                int y = A[j];
                int d = x - y;
                
                # We at least have a minimum chain length of 2 now,
                # given that (A[j], A[i]) with the difference d, 
                # by default forms a chain of length 2.
                int len = 2;  
                
                if (dp[j].containsKey(d)) {
                    # At index j, if we had already seen a difference d,
                    # then potentially, we can add A[i] to the same chain
                    # and extend it by length 1.
                    len = dp[j].get(d) + 1;
                }
                
                # Obtain the maximum chain length already seen so far at index i 
                # for the given differene d;
                int curr = dp[i].getOrDefault(d, 0);
                
                # Update the max chain length for difference d at index i.
                dp[i].put(d, Math.max(curr, len));
                
                # Update the global max.
                longest = Math.max(longest, dp[i].get(d));
            }
        }
      
        return longest;
    }
}

def longestArithSeqLength(A):
	longest = 0
	n = len(A)
	# dp[i] = dictionary of differences seen so far 
	dp = [{}] * len(A)
	# key = difference
	# value = max(curr, length)
	for i in range(1, n): # for each element A[i]
		for j in range(0, i): # iterate over the values to the left of i
			d = A[i] - A[j] # compute the difference, d
			length = 2 # default minimum sequence length is 2
			if d in dp[j]: # if we have seen this diff before, we can extend it by 1.
				length = dp[i][d] + 1
			# Obtain the maximum chain length already seen so far at index i 
            # for the given differene d;
			curr = dp[i][d] if d in dp[i] else 0
			dp[i][d] = max(curr, length) # Update the max chain length for difference d at index i.
			longest = max(longest, dp[i][d]) # update the global max
	return longest

def longestArithSeqLength(self, A: List[int]):
	dp = {}
	for i, a2 in enumerate(A[1:], start=1):
		for j, a1 in enumerate(A[:i]):
			d = a2 - a1
			if (j, d) in dp:
				dp[i,d] = dp[j,d] + 1
			else:
				dp[i,d] = 2
	return max(dp.values())


def longestArithSeqLength(A):
	dp = {}
	for i in range(1, len(A)):
		for j in range(0, i):
			d = A[j] - A[i]
			if (j, d) in dp:
				dp[i,d] = dp[j,d] + 1
			else:
				dp[i,d] = 2
	return max(dp.values())

















