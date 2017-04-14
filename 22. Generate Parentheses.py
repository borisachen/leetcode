"""Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

public List<String> generateParenthesis(int n) {
    List<String> list = new ArrayList<String>();
    backtrack(list, "", 0, 0, n);
    return list;
}

public void backtrack(List<String> list, String str, int open, int close, int max){
    
    if(str.length() == max*2){
        list.add(str);
        return;
    }
    
    if(open < max)
        backtrack(list, str+"(", open+1, close, max);
    if(close < open)
        backtrack(list, str+")", open, close+1, max);
}
"""

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        def backtrack(res, temp, nopen, nclose, max):
        	if len(temp)==max*2:
        		res.append(temp)
        		return
        	if nopen < max:
        		backtrack(res, temp+'(', nopen+1, nclose, max)
        	if nclose < nopen:
        		backtrack(res, temp+')', nopen, nclose+1, max)
        backtrack(res, "", 0,0,n)
        return res

s=Solution()
s.generateParenthesis(3)