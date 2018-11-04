271. Encode and Decode Strings

Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

Machine 1 (sender) has the function:

string encode(vector<string> strs) {
  // ... your code
  return encoded_string;
}
Machine 2 (receiver) has the function:
vector<string> decode(string s) {
  //... your code
  return strs;
}
So Machine 1 does:

string encoded_string = encode(strs);
and Machine 2 does:

vector<string> strs2 = decode(encoded_string);
strs2 in Machine 2 should be the same as strs in Machine 1.

Implement the encode and decode methods.

Note:
The string may contain any possible characters out of 256 valid ascii characters. Your algorithm should be generalized enough to work on any possible characters.
Do not use class member/global/static variables to store states. Your encode and decode algorithms should be stateless.
Do not rely on any library method such as eval or serialize methods. You should implement your own encode/decode algorithm.

-----
Using a special character alone wont work since any string can contain it.
But if we also use the length of each string, then we know how to search.

len(s1):s1:len(s2):s2:...
-----

def encode(strs):
	res = ''
	for word in strs:
		res += str(len(word)) + ':' + str(word)
	return res

def decode(encoded_string):
	len_len = encoded_string.find(':')
	res = []
	while len_len > -1:
		print(encoded_string)
		word_len = int(encoded_string[0:len_len])
		word = encoded_string[len_len+1:len_len+word_len+1]
		res.append(word)
		encoded_string = encoded_string[len_len+word_len+1:]
		len_len = encoded_string.find(':')
	return res

es = encode(['hello','world.','.','foobar'])
decode(es)
