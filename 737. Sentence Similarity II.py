737. Sentence Similarity II

Given two sentences words1, words2 (each represented as an array of strings), and a list of similar word pairs pairs, determine if two sentences are similar.

For example, words1 = ["great", "acting", "skills"] and words2 = ["fine", "drama", "talent"] are similar, if the similar word pairs are pairs = [["great", "good"], ["fine", "good"], ["acting","drama"], ["skills","talent"]].

Note that the similarity relation is transitive. For example, if "great" and "good" are similar, and "fine" and "good" are similar, then "great" and "fine" are similar.

Similarity is also symmetric. For example, "great" and "fine" being similar is the same as "fine" and "great" being similar.

Also, a word is always similar with itself. For example, the sentences words1 = ["great"], words2 = ["great"], pairs = [] are similar, even though there are no specified similar word pairs.

Finally, sentences can only be similar if they have the same number of words. So a sentence like words1 = ["great"] can never be similar to words2 = ["doubleplus","good"].

Note:

The length of words1 and words2 will not exceed 1000.
The length of pairs will not exceed 2000.
The length of each pairs[i] will be 2.
The length of each words[i] and pairs[i][j] will be in the range [1, 20].

-----
Approach 1:
We can preprocess everything into dictionaries to allow for quick lookup.
ideally we want :
{'great':['good', 'fine']} and all permutations of that, so we can do O(1) look ups to see if the word is valid synonym.
preprocessing should take O(n), where n = number of word pairs.
Once we have the dictionary, takes O(m) to iterate through where m=length of query, so total time complexity is O(n+m)
-----

words1 = ["great", "acting", "skills"] 
words2 = ["fine", "drama", "talent"]
pairs = [["great", "good"], ["fine", "good"], ["acting","drama"], ["skills","talent"]]


def dfs(source, target, visited, d):
	if target in d[source]:
		return True
	visited.add(source)
	for next in d[source]:
		if (next not in visited) and next == target:
			return True
		if (next not in visited) and dfs(next, target, visited, d):
			return True
	return False

def sent_sim(words1, words2, pairs):
	if len(words1) != len(words2):
		return(False)
	# build the dictionary
	d = {}
	for term in pairs:
		t0 = term[0]
		t1 = term[1]
		if t0 not in d:
			d[t0] = []
		if t1 not in d:
			d[t1] = []
		d[t0].append(t1)
		d[t1].append(t0)
	# check each word 
	for i in range(len(words1)):
		w1 = words1[i]
		w2 = words2[i]
		if (w1 == w2): 
			continue
		if (w1 not in d[w2]) or (w2 not in d[w1]):
			return(False)
		if dfs(w1, w2, set(), d):
			return(False)
	return (True)

sent_sim(words1, words2, pairs)

