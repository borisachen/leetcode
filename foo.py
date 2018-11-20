
words1 = ["great", "acting", "skills"] 
words2 = ["fine", "drama", "talent"]
pairs = [["great", "good"], ["fine", "good"], ["acting","drama"], ["skills","talent"]]

-----

def areSentencesSimilarTwo(words1, words2, pairs):
	if len(words1)!=len(words2): return False

d = {}
for w1, w2 in pairs:
	if w1 not in d: d[w1] = []
	if w2 not in d: d[w2] = []
	d[w1].append(w2)
	d[w2].append(w1)

for src, tgt in zip(words1, words2):
	seen = {src}
	stack = [src]
	while stack:
		word = stack.pop()
		if word == tgt: break
		for nextword in d[word]:
			if nextword not in seen:
				seen.add(nextword)
				stack.append(nextword)
	else: return False
return True
