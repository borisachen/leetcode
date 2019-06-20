1000. Minimum Cost to Merge Stones
Hard/106/10

There are N piles of stones arranged in a row.  The i-th pile has stones[i] stones.

A move consists of merging exactly K consecutive piles into one pile, and the cost of this move is equal to the total number of stones in these K piles.

Find the minimum cost to merge all piles of stones into one pile.  If it is impossible, return -1.



Example 1:

Input: stones = [3,2,4,1], K = 2
Output: 20
Explanation:
We start with [3, 2, 4, 1].
We merge [3, 2] for a cost of 5, and we are left with [5, 4, 1].
We merge [4, 1] for a cost of 5, and we are left with [5, 5].
We merge [5, 5] for a cost of 10, and we are left with [10].
The total cost was 20, and this is the minimum possible.
Example 2:

Input: stones = [3,2,4,1], K = 3
Output: -1
Explanation: After any merge operation, there are 2 piles left, and we can't merge anymore.  So the task is impossible.
Example 3:

Input: stones = [3,5,1,2,6], K = 3
Output: 25
Explanation:
We start with [3, 5, 1, 2, 6].
We merge [5, 1, 2] for a cost of 8, and we are left with [3, 8, 6].
We merge [3, 8, 6] for a cost of 17, and we are left with [17].
The total cost was 25, and this is the minimum possible.


Note:

1 <= stones.length <= 30
2 <= K <= 30
1 <= stones[i] <= 100

State
transition
init
answer


public int mergeStonesTwo(int[] stones) {
    if (stones == null || stones.length == 0) {
        return 0;
    }
    int len = stones.length;
    int max = Integer.MAX_VALUE;
    int[][] dp = new int[len + 1][len + 1];
    int[] prefixSum = new int[len + 1];
    int i, j, k, l;
    for (i = 1; i <= len; i++) {
        prefixSum[i] = prefixSum[i - 1] + stones[i - 1];
    }

    for (i = 1; i <= len; i++) {
        dp[i][i] = 0;
    }

    for (l = 2; l <= len; l++) {
        for (i = 1; i <= len - l + 1; i++) {
            j = i + l - 1;
            dp[i][j] = max;
            int sum = prefixSum[j] - prefixSum[i - 1];
            for (k = i; k < j; k++) {
                dp[i][j] = Math.min(dp[i][j], dp[i][k] + dp[k + 1][j] + sum);
            }
        }
    }

    return dp[1][len];
}