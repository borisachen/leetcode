752. Open the Lock
Medium/279/18

You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. The wheels can rotate freely and wrap around: for example we can turn '9' to be '0', or '0' to be '9'. Each move consists of turning one wheel one slot.

The lock initially starts at '0000', a string representing the state of the 4 wheels.

You are given a list of deadends dead ends, meaning if the lock displays any of these codes, the wheels of the lock will stop turning and you will be unable to open it.

Given a target representing the value of the wheels that will unlock the lock, return the minimum total number of turns required to open the lock, or -1 if it is impossible.

Example 1:
Input: deadends = ["0201","0101","0102","1212","2002"], target = "0202"
Output: 6
Explanation:
A sequence of valid moves would be "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202".
Note that a sequence like "0000" -> "0001" -> "0002" -> "0102" -> "0202" would be invalid,
because the wheels of the lock become stuck after the display becomes the dead end "0102".
Example 2:
Input: deadends = ["8888"], target = "0009"
Output: 1
Explanation:
We can turn the last wheel in reverse to move from "0000" -> "0009".
Example 3:
Input: deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888"
Output: -1
Explanation:
We can't reach the target without getting stuck.
Example 4:
Input: deadends = ["0000"], target = "8888"
Output: -1
Note:
The length of deadends will be in the range [1, 500].
target will not be in the list deadends.
Every string in deadends and the string target will be a string of 4 digits from the 10,000 possibilities '0000' to '9999'.
-----
Approach 1: DFS/Backtracking
This hits max recurrsion error.

Approach 2: BFS with a queue
Its important to keep a visited set

Approach 3: Bidirectional BFS
-----
# DFS / backtracking
class Solution:
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        res = []
        self.back(['0000'], '0000', res, target, deadends)
        return min(res)
    def back(self, path, temp, res, tgt, dead):
        if temp == tgt:
            res.append(len(path))
            return
        if temp in dead:
            return
        for i in range(4):
            for j in [-1, 1]:
                cand = temp[:i] + str((int(temp[i])+j) % 10) + temp[i+1:]
                if cand not in dead and cand not in path:
                    path.append(cand)
                    self.back(path, cand, res, tgt, dead)
                    _ = path.pop()

# Regular BFS
class Solution:
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        depth = 1
        if '0000' in deadends: return -1
        q = {'0000'}
        visited = {'0000'}
        while q:
            next = set()
            for item in q:
                for i in range(4):
                    for j in [-1,1]:
                        cand = item[:i] + str((int(item[i])+j) % 10) + item[i+1:]
                        if cand == target: return depth
                        if cand not in deadends and cand not in visited:
                            next.add(cand)
                            visited.add(cand)
            if not next: return -1
            q = next
            depth += 1
        return -1


# Bi-directional BFS
class Solution:
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        depth = 1
        if '0000' in deadends: return -1
        if target == '0000': return 0
        top = {'0000'}
        bot = {target}
        visited = {'0000'}
        side = 1
        while top and bot:
            cur = top if side == 1 else bot
            next = set()
            for item in cur:
                for i in range(4):
                    for j in [-1,1]:
                        cand = item[:i] + str((int(item[i])+j) % 10) + item[i+1:]
                        if side == 1 and cand in bot: return depth
                        if side == -1 and cand in top: return depth
                        if cand not in deadends and cand not in visited:
                            next.add(cand)
                            visited.add(cand)
            if side == 1:
                top = next
            else:
                bot = next
            side *= -1
            depth += 1
        return -1
