266. Palindrome Permutation
Easy (locked)

Given a string, determine if a permutation of the string could form a palindrome.

For example,
"code" -> False, "aab" -> True, "carerac" -> True.

-----------------------------------
We can put them in a hashmap/dict.
all values must be even, except we can have one odd.
Time: O(n) to create the hashmap. another pass to check evens/odds
Space: O(1) since we have 128 max keys

Another option: use a set
if a char is already in the set, we can remove it
at the end, check if the size of the set is <= 1
-----------------------------------

def palin_perm(s):
	d = {}
	for char in s:
		if char not in d:
			d[char] = 1
		else:
			d[char] += 1
	num_odd = 0
	for value in d.values():
		if value % 2 == 1:
			num_odd += 1
	return num_odd <= 1

palin_perm('code')
palin_perm('aab')
palin_perm('carerac')

public class Solution {
    public boolean canPermutePalindrome(String s) {
        Set < Character > set = new HashSet < > ();
        for (int i = 0; i < s.length(); i++) {
            if (!set.add(s.charAt(i)))
                set.remove(s.charAt(i));
        }
        return set.size() <= 1;
    }
}
