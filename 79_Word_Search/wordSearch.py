"""
Question to ask:
1). the letters doen't necessarily come from one row/column? (Yes)
2). Does the order in board matters? Ex. ['e', 's', 'e'], word = 'see' => True? (order matters)
3). One letter can only be used once? (Yes)
4). Does upper case and lower case make difference?
5). Can board contain "" letter?

Solution:
backtracking(or dfs):
First find the matched characters in board with first character in word and start recursively searching in four direction.
Use an 2d array visited to mark if a letter is already used in current branch
"""

class Solution(object):
    def exist(self, board, word):
        """
        :type board: list[str]
        :type word : str
        :rtype     : bool
        """
        #sanity check
        if len(word) == 0 or len(board) == 0:
            return False

        #serach the match for the first letter
        n, m = len(board), len(board[0])
        visited = [ [0] * m for _ in xrange(n)]
        res = False

        for i in xrange(n):
            for j in xrange(m):
                if board[i][j] == word[0]:
                    #set the cell(i, j) as visited for current branch search
                    visited[i][j] = 1

                    res |= self.btSearch(board,i,j, word[1:], visited)

                    #restore the cell(i,j) as unvisited
                    visited[i][j] = 0

        return res

    # @param board: list[str], board representation
    # @param i, j : int, board[i][j] is the center which current branch searches from 
    # @param word : current sub word to search
    # @param visited: list[list[int]], two dimention array, visited[i][j] represent if board[i][j] is visited or not in current branch
    def btSearch(self, board, i, j, word, visited):
        if word == "":
            return True

        res = False

        #backtracking to go four directrions, north, south, east, west
        for ni, nj in [ [i-1, j], [i, j-1], [i+1, j], [i,j+1]]:
            if ni >= 0 and ni < len(board) and nj >= 0 and nj < len(board[0]) and board[ni][nj] == word[0] and visited[ni][nj] == 0:
                visited[ni][nj] = 1
                res |= self.btSearch(board, ni, nj, word[1:], visited)
                if res == True:
                    return res
                visited[ni][nj] = 0

        return res
