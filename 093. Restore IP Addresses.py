93. Restore IP Addresses

Given a string containing only digits, restore it by returning all possible valid IP address combinations.

For example:
Given "25525511135",

return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)


class Solution(object):
	def restoreIpAddresses(self, s):
		"""
		:type s: str
		:rtype: List[str]
		"""
		res = []
		self.backtrack(s, res, 0, '', 0)
		return res

	def backtrack(self, ip, res, start, temp, count):
		if count > 4:
			return
		if count == 4 and start==len(ip):
			res.append(temp)
		for i in range(1,4):
			if start+i > len(ip):
				break
			next_block = ip[start:(start+i)]
			# check for invalid blocks
			if (next_block[0]=='0' and len(next_block)>1) or (i==3 and next_block > '255'):
				continue
			period = '.' if count < 3 else ''
			a = "" if count == 3 else "."
			self.backtrack(ip, res, start+i, temp+next_block+a, count+1)


class Solution(object):
	def restoreIpAddresses(self, s):
		"""
		:type s: str
		:rtype: List[str]
		"""
		solutions = []
		self.restoreIp(ip=s, solutions=solutions, idx=0, restored="", count=0)
		return solutions

	def restoreIp(self, ip, solutions, idx, restored, count):
		if count > 4: 
			return
		if count==4 and idx==len(ip):
			solutions.append(restored)
		for i in range(1,4): # i is the number of digits to try for the next set. try i=1,2,3
			if idx+i > len(ip): # if we are beyond the original ip, break the loop entirely
				break
			s = ip[idx:(idx+i)] # s = the current next value to be added
			if (s[0]=='0' and len(s)>1) or (i==3 and s>='256'): # s is invalid if it starts with 0XX or is greater than 255
				continue
			a = "" if count == 3 else "." # what to append after s? either . or nothing depending on current count of .'s
			self.restoreIp(ip, solutions, idx+i, restored+s+a, count+1)






public List<String> restoreIpAddresses(String s) {
    List<String> solutions = new ArrayList<String>();
    restoreIp(s, solutions, 0, "", 0);
    return solutions;
}

private void restoreIp(String ip, List<String> solutions, int idx, String restored, int count) {
    if (count > 4) return;
    if (count == 4 && idx == ip.length()) solutions.add(restored);
    
    for (int i=1; i<4; i++) {
        if (idx+i > ip.length()) break;
        String s = ip.substring(idx,idx+i);
        if ((s.startsWith("0") && s.length()>1) || (i==3 && Integer.parseInt(s) >= 256)) continue;
        restoreIp(ip, solutions, idx+i, restored+s+(count==3?"" : "."), count+1);
    }
}





