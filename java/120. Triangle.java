120. Triangle

Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:
Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.

public class Solution {
	public int minimumTotal(List<List<Integer>> triangle) {
		int n = triangle.size();
		int[] dp = new int[n];
		for (int k=0; k<n; k++) {
		    dp[k] = triangle.get(n-1).get(k);
		}
		for (int j=n-2; j>=0; j--) {
			for (int i=0; i<j+1; i++) {
				dp[i] = Math.min(dp[i], dp[i+1]) + triangle.get(j).get(i);
			}
		}
		return dp[0];
	}
}