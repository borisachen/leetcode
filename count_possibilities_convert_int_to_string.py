Count Possibilities

We have a dictionary with 
a:1
b:2
...
z:26
Given a string = '11135213',
we want to find the number of possibilities that the string forms.
11 -> 1,1 or 11
Whenever we find a 1 or a 2, we need to look ahead see if we need to create a second branch.


def dfs(query, keys):
	if query == '':
		return 0
	if len(query) >= 2 and int(query[0:2]) <= 26:
		return 1 + dfs(query[1:], keys) + dfs(query[2:], keys)
	else:
		return dfs(query[1:], keys)


def count_possibilities(query):
	keys = {}
	for i,j in enumerate('abcdefghijklmnopqrstuvwxyz'):
		keys[str(i)] = j
	return dfs(query, keys) + 1


count_possibilities(query = '1') # 1
count_possibilities(query = '11')  # 2
count_possibilities(query = '111') # 3
count_possibilities(query = '1111') # 5
count_possibilities(query = '2') # 1
count_possibilities(query = '26') # 2
count_possibilities(query = '27') # 1
