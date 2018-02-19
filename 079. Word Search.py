79. Word Search

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

For example,
Given board =

[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.


class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        nrow = len(board)
        ncol = len(board[0])
        for i in range(nrow):
            for j in range(ncol):
                if self.dfs(word, i, j, board):
                    return True
        return False
        
    def dfs(self, word, i, j, board):
        if len(word)==0:
            return True
        if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or word[0] != board[i][j]:
            return False
        tmp = board[i][j]
        board[i][j] = '#'
        res = (self.dfs(word[1:], i+1, j, board) or
                self.dfs(word[1:], i-1, j, board) or
                self.dfs(word[1:], i, j+1, board) or
                self.dfs(word[1:], i, j-1, board)
            )
        board[i][j] = tmp
        return res