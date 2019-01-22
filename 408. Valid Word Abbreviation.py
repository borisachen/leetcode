408. Valid Word Abbreviation
Easy ?/?
https://leetfree.com/problems/valid-word-abbreviation.html

Given a non-empty string s and an abbreviation abbr, return whether the string matches with the given abbreviation.

A string such as "word" contains only the following valid abbreviations:

["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]
Notice that only the above abbreviations are valid abbreviations of the string "word". Any other string is not a valid abbreviation of "word".

Note:
Assume s contains only lowercase letters and abbr contains only lowercase letters and digits.

Example 1:
Given s = "internationalization", abbr = "i12iz4n":
Return true.

Example 2:
Given s = "apple", abbr = "a2e":

Return false.
-----
-----

def validwordabbr(s, abbr):
    i = j = 0
    n = len(s)
    m = len(abbr)
    if not s and not abbr: return True
    if not s or not abbr: return False
    while i < n and j < m:
        print(i,s[i],j, abbr[j])
        if abbr[j].isdigit() == False:
            if abbr[j] != s[i]:
                return False
        else:
            k = j
            while k < m and abbr[k].isdigit():
                k += 1
            i += int(abbr[j:k]) - 1
            j = k-1
        j += 1
        i += 1
        if (i < n) != (j < m):
            return False
    return True

validwordabbr(s = "apple", abbr = "a2e")
validwordabbr(s = "internationalization", abbr = "i12iz4n")
