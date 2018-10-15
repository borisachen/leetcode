249. Group Shifted Strings

Given a string, we can "shift" each of its letter to its successive letter, 
for example, "abc" -> "bcd". We can keep "shifting" which forms the sequence,

"abc" -> "bcd" -> ... -> "xyz"
Given a list of strings which contains only lowercase alphabets, group all strings that belong to the same shifting sequence.

For example, given: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"], 
A solution is:

[
  ["abc","bcd","xyz"],
  ["az","ba"],
  ["acef"],
  ["a","z"]
]
---------------
Approach 1:
Notice that if we take ord(char) and then look at the difference of each pair of characters,
then we get a unique key for each string. 
The difference we should mod by 26 for the wrap around.
Once we have a key for each string, we build a dictionary.

Complexity:
Populating the dictionary is a for loop over n words. 
each word we take ord of all characters twice, so if m is the longest word length,
O(num words * len avg word)
Space: O(n)
---------------

def get_key(s):
	res = [str((ord(s[i+1])-ord(s[i]))%26) for i in range(len(s)-1)]
	return ':'.join(res)

def grp_shifted(given):
	dic = {}
	for word in given:
		key = get_key(word)
		if key in dic:
			dic[key].append(word)
		else:
			dic[key] = [word]
	res = []
	for key in dic.keys():
		res.append(dic[key])
	return res	

grp_shifted(given = ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"])