418. Sentence Screen Fitting

Given a rows x cols screen and a sentence represented by a list of non-empty words, find how many times the given sentence can be fitted on the screen.

Note:

A word cannot be split into two lines.
The order of words in the sentence must remain unchanged.
Two consecutive words in a line must be separated by a single space.
Total words in the sentence wont exceed 100.
Length of each word is greater than 0 and wont exceed 10.
1 ≤ rows, cols ≤ 20,000.
Example 1:

Input:
rows = 2, cols = 8, sentence = ["hello", "world"]

Output: 
1

Explanation:
hello---
world---

The character '-' signifies an empty space on the screen.
Example 2:

Input:
rows = 3, cols = 6, sentence = ["a", "bcd", "e"]

Output: 
2

Explanation:
a-bcd- 
e-a---
bcd-e-

The character '-' signifies an empty space on the screen.
Example 3:

Input:
rows = 4, cols = 5, sentence = ["I", "had", "apple", "pie"]

Output: 
1

Explanation:
I-had
apple
pie-I
had--

The character '-' signifies an empty space on the screen.

-------------------------
Naive:
Try to fill row by row, adding the words one at a time.
When it no longer fits, move to the next line.
When we fill the last word, up the counter and restart.
When we have filled the last row, return the counter.
n = number of words,
m = avg len of words
r = rows
c = columns
Time: O(r*c/m)

Note: - Eventually we will hit a cycle. At that point there is no need to repeat the searching.

Rather than interating on the emtpy matrix, we could concat the sentence and move to the c-th
position, then find earlist word that fits up to slot c. Then we truncate the sentence and 
repeat.

------------------------------


