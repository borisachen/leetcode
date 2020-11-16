301. Remove Invalid Parentheses
Hard/2930/131

Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Example 1:

Input: "()())()"
Output: ["()()()", "(())()"]

Example 2:

Input: "(a)())()"
Output: ["(a)()()", "(a())()"]

Example 3:

Input: ")("
Output: [""]

"""
Key Points:
- Generate unique answer once and only once, do not rely on Set.
- Do not need preprocess.

Explanation:
We all know how to check a string of parentheses is valid using a stack. Or even simpler use a counter.
The counter will increase when it is ‘(‘ and decrease when it is ‘)’. 
Whenever the counter is negative, we have more ‘)’ than ‘(‘ in the prefix.

To make the prefix valid, we need to remove a ‘)’. T
he problem is: which one? The answer is any one in the prefix. 
However, if we remove any one, we will generate duplicate results, for example: s = ()), we can remove s[1] or s[2] but the result is the same (). 
Thus, we restrict ourself to remove the first ) in a series of concecutive )s.

After the removal, the prefix is then valid. We then call the function recursively to solve the rest of the string. However, we need to keep another information: the last removal position. If we do not have this position, we will generate duplicate by removing two ‘)’ in two steps only with a different order.
For this, we keep tracking the last removal position and only remove ‘)’ after that.

Now one may ask. What about ‘(‘? What if s = ‘(()(()’ in which we need remove ‘(‘?
The answer is: do the same from right to left.
However a cleverer idea is: reverse the string and reuse the code!
Here is the final implement in Java.

class Solution {
    public List<String> removeInvalidParentheses(String s) {
        List<String> output = new ArrayList<>();
        removeHelper(s, output, 0, 0, '(', ')');
        return output;
    }

    public void removeHelper(String s, List<String> output, int iStart, int jStart, char openParen, char closedParen) {
        int numOpenParen = 0, numClosedParen = 0;
        for (int i = iStart; i < s.length(); i++) {
            if (s.charAt(i) == openParen) numOpenParen++;
            if (s.charAt(i) == closedParen) numClosedParen++;
            if (numClosedParen > numOpenParen) { // We have an extra closed paren we need to remove
                for (int j = jStart; j <= i; j++) // Try removing one at each position, skipping duplicates
                    if (s.charAt(j) == closedParen && (j == jStart || s.charAt(j - 1) != closedParen))
                    // Recursion: iStart = i since we now have valid # closed parenthesis thru i. jStart = j prevents duplicates
                        removeHelper(s.substring(0, j) + s.substring(j + 1, s.length()), output, i, j, openParen, closedParen);
                return; // Stop here. The recursive calls handle the rest of the string.
            }
        }
        // No invalid closed parenthesis detected. Now check opposite direction, or reverse back to original direction.
        String reversed = new StringBuilder(s).reverse().toString();
        if (openParen == '(')
            removeHelper(reversed, output, 0, 0, ')','(');
        else
            output.add(reversed);
    }
}
"""

class Solution(object):
	def removeInvalidParentheses(self, s):
		"""
		:type s: str
		:rtype: List[str]
		"""
		output = []
		self.removeHelper(s, output, 0, 0)
		return output

	def removeHelper(self, s, output, iStart, jStart, openParen, closedParen):
		numopen, numclosed = 0, 0
		for i in range(iStart, len(s)):
			if s[i] == openParen: numopen += 1
			if s[i] == closedParen: numclosed += 1
			if numclosed > numopen: # we have an extra closed one we need to remove
				# try removing one at each position, skipping duplicates
				for j in range(jStart, i+1):
					if s[j] == ')' and (j == jStart or s[j-1] != '('):
						# recusion; istart = i.  since we now have valid # closed parenthesis thru i. 
						# 	jstart = j prevent duplicates
						self.removeHelper(s[0:j]+s[j+1:len(s)], ouptput, i, j, openParen, closedParen)
				return
		# no invalid closed parenthesis detected. now check opposite direction, or reverse back to original direction
		s_reversed = s[::-1]
		if openParen == '(':
			self.removeHelper(s_reversed, output, 0, 0, ')', '(')
		else:
			output.append(s_reversed)



"""
Here I share my DFS or backtracking solution. It's 10X faster than optimized BFS.

Limit max removal rmL and rmR for backtracking boundary. Otherwise it will exhaust all possible valid substrings, not shortest ones.
Scan from left to right, avoiding invalid strs (on the fly) by checking num of open parens.
If it's '(', either use it, or remove it.
If it's '(', either use it, or remove it.
Otherwise just append it.
Lastly set StringBuilder to the last decision point.
In each step, make sure:

i does not exceed s.length().
Max removal rmL rmR and num of open parens are non negative.
De-duplicate by adding to a HashSet.
Compared to 106 ms BFS (Queue & Set), it's faster and easier. Hope it helps! Thanks.

public List<String> removeInvalidParentheses(String s) {
    int rmL = 0, rmR = 0;
    for (int i = 0; i < s.length(); i++) {
        if (s.charAt(i) == '(') {
            rmL++;
        } else if (s.charAt(i) == ')') {
            if (rmL != 0) {
                rmL--;
            } else {
                rmR++;
            }
        }
    }
    Set<String> res = new HashSet<>();
    dfs(s, 0, res, new StringBuilder(), rmL, rmR, 0);
    return new ArrayList<String>(res);
}

public void dfs(String s, int i, Set<String> res, StringBuilder sb, int rmL, int rmR, int open) {
    if (rmL < 0 || rmR < 0 || open < 0) {
        return;
    }
    if (i == s.length()) {
        if (rmL == 0 && rmR == 0 && open == 0) {
            res.add(sb.toString());
        }        
        return;
    }
    char c = s.charAt(i); 
    int len = sb.length();
    if (c == '(') {
        dfs(s, i + 1, res, sb, rmL - 1, rmR, open);		    // not use (
    	dfs(s, i + 1, res, sb.append(c), rmL, rmR, open + 1);       // use (

    } else if (c == ')') {
        dfs(s, i + 1, res, sb, rmL, rmR - 1, open);	            // not use  )
    	dfs(s, i + 1, res, sb.append(c), rmL, rmR, open - 1);  	    // use )

    } else {
        dfs(s, i + 1, res, sb.append(c), rmL, rmR, open);	
    }
    sb.setLength(len);        
}
"""

class Solution(object):
	def removeInvalidParentheses(self, s):
		"""
		:type s: str
		:rtype: List[str]
		"""
		rmL = 0 # number of ( to remove
		rmR = 0 # number of ) to remove
		for i in range(len(s)):
			if s[i] == '(':
				rmL += 1
			elif s[i] == ')':
				if rmL != 0: 
					rmL -= 1
				else: 
					rmR += 1
		res = set()
		self.dfs(s, 0, res, '', rmL, rmR, 0)
		return list(res)

	def dfs(self, s, i, res, sb, rmL, rmR, nopen):
		if rmL < 0 or rmR < 0 or nopen < 0:
			return
		if i == len(s):
			if rmL == 0 and rmR == 0 and nopen == 0:
				res.add(sb)
			return
		c = s[i]
		if c == '(':
			self.dfs(s, i+1, res, sb, rmL-1, rmR, nopen) # not use
			self.dfs(s, i+1, res, sb+c, rmL, rmR, nopen+1) # use it
		elif c == ')':
			self.dfs(s, i+1, res, sb, rmL, rmR-1, nopen) # do not use
			self.dfs(s, i+1, res, sb+c, rmL, rmR, nopen-1) # use
		else:
			self.dfs(s, i+1, res, sb+c, rmL, rmR, nopen)



























