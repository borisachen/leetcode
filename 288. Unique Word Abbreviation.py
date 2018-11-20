288. Unique Word Abbreviation

An abbreviation of a word follows the form <first letter><number><last letter>. Below are some examples of word abbreviations:

a) it                      --> it    (no abbreviation)

     1
b) d|o|g                   --> d1g

              1    1  1
     1---5----0----5--8
c) i|nternationalizatio|n  --> i18n

              1
     1---5----0
d) l|ocalizatio|n          --> l10n

Assume you have a dictionary and given a word, 
find whether its abbreviation is unique in the dictionary. 
A words abbreviation is unique if no other word from the dictionary has the same abbreviation.

Example: 
Given dictionary = [ "deer", "door", "cake", "card" ]

isUnique("dear") -> false
isUnique("cart") -> true
isUnique("cane") -> false
isUnique("make") -> true

-----
We can make the abbreviation for all words in the dictionary.
Keep the results in a hashmap. ad={abbrev:count} then wd={word:abbrev}
Then given a query word, do a lookup for the abbrev, then look up the count.
Preprocessing: O(n*L) where n = size of dictionary, L = avg length of words.
Query time: O(1)
Space: O(n)

Actually, we dont need a dictionary of lists. We can just keep a master set.
-----

import collections
dic = [ "deer", "door", "cake", "card" ]
query = 'dear'

def get_abbrev(word):
	wordlen = len(word)
	gaplen = max(wordlen-2, 0)
	abbrev = word[0] + str(gaplen) + word[-1]
	return abbrev

def unique_word_abbrev(dic, query):
	ad = collections.defaultdict(int)
	wd = collections.defaultdict(str)
	sd = set()
	for word in dic:
		abbrev = get_abbrev(word)
		wd[word] = abbrev
		ad[abbrev] += 1
		set.add(word)
	abbrev_query = get_abbrev(query)
	if abbrev_query not in ad: return True
	elif ad[abbrev_query] == 1: 
		if query in sd: return True
		else: return False
	else: return False

unique_word_abbrev(dic, 'dear')
unique_word_abbrev(dic, 'cart')
unique_word_abbrev(dic, 'cane')
unique_word_abbrev(dic, 'make')



