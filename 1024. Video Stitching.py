1024. Video Stitching
Medium/439/21

You are given a series of video clips from a sporting event that lasted T seconds.  
These video clips can be overlapping with each other and have varied lengths.

Each video clip clips[i] is an interval: it starts at time clips[i][0] and ends at time clips[i][1].  
We can cut these clips into segments freely: for example, a clip [0, 7] can be cut into segments [0, 1] + [1, 3] + [3, 7].

Return the minimum number of clips needed so that we can cut the clips into segments that cover the entire sporting event ([0, T]).  
If the task is impossible, return -1.



Example 1:

Input: clips = [[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]], T = 10
Output: 3
Explanation:
We take the clips [0,2], [8,10], [1,9]; a total of 3 clips.

Then, we can reconstruct the sporting event as follows:
We cut [1,9] into segments [1,2] + [2,8] + [8,9].
Now we have segments [0,2] + [2,8] + [8,10] which cover the sporting event [0, 10].


Example 2:

Input: clips = [[0,1],[1,2]], T = 5
Output: -1
Explanation:
We cant cover [0,5] with only [0,1] and [0,2].


Example 3:

Input: clips = [[0,1],[6,8],[0,2],[5,6],[0,4],[0,3],[6,7],[1,3],[4,7],[1,4],[2,5],[2,6],[3,4],[4,5],[5,7],[6,9]], T = 9
Output: 3
Explanation:
We can take clips [0,4], [4,7], and [6,9].


Example 4:

Input: clips = [[0,4],[2,8]], T = 5
Output: 2
Explanation:
Notice you can have extra video after the event ends.


Constraints:

1 <= clips.length <= 100
0 <= clips[i][0] <= clips[i][1] <= 100
0 <= T <= 100

"""
# 1. Sort -- 
time nlogn, 
space 1

"""

def videoStitching(self, clips, T):
    end = -1 
    end2 = 0 # pointer for how much time we have captured.
    res = 0 # counter for number of clips used
    clips = sorted(clips)
    for i, j in clips:
        if end2 >= T or i > end2:
            break
        elif end < i <= end2: # if i exceeds the current 
            res = res + 1
            end = end2
        end2 = max(end2, j)
    return res if end2 >= T else -1


"""
Solution 2: Sort + DP

Sort clips first.
let dp[i] = minimum number of clips needed to get to time i
Then for each clip, update dp[clip[0]] ~ dp[clip[1]].
transition function: dp[i] = min(dp[i], dp[clip[0]]+1)
Time O(NlogN + NT), Space O(T)

int videoStitching(vector<vector<int>>& clips, int T) {
    sort(clips.begin(), clips.end());
    vector<int> dp(101, 101);
    dp[0] = 0;
    for (auto& c : clips)
        for (int i = c[0] + 1; i <= c[1]; i++)
            dp[i] = min(dp[i], dp[c[0]] + 1);
    return dp[T] >= 100 ? -1 : dp[T];
}
"""

class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        clips=sorted(clips)
        # dp[i] = min number of clips needed to get to timestep i
        dp = [101] * 101 
        for clip in clips:
            for i in range(clip[0] + 1, clip[1]+1):
            	# transition: dp[i] = minimum of 
            	#  dp[i]
            	#  dp[start index of this clip] + 1
                dp[i] = min(dp[i], dp[clip[0]]+1)
        return dp[T] if dp[T] < 101 else -1
        # time - O(n log n + n*T)
        # space = O(T)

"""
Solution 3: DP

Loop on i form 0 to T,
loop on all clips,
If clip[0] <= i <= clip[1], we update dp[i]

Time O(NT), Space O(T)

Java

public int videoStitching(int[][] clips, int T) {
    int[] dp = new int[T + 1];
    Arrays.fill(dp, T + 1);
    dp[0] = 0;
    for (int i = 1; i <= T && dp[i - 1] < T; i++) {
        for (int[] c : clips) {
            if (c[0] <= i && i <= c[1])
                dp[i] = Math.min(dp[i], dp[c[0]] + 1);
        }
    }
    return dp[T] == T + 1 ? -1 : dp[T];
}
"""

def videostitching(clips, T):
	dp = [0] * (T+1)
	dp[0] = 0
	# for each time step (0, T+1)
	for i in range(1, T+1):
		for c in clips:
			if c[0] <= i <= c[1]:
				dp[i] = min(dp[i], dp[c[0]]+1)
	return dp[T]
	# time - O(N*T)
	# space - O(T)

