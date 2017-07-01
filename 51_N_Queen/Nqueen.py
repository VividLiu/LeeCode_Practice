"""
Solution: 
Backtracking
Space complexity: O(n) for the extra board variable, the return variable is not considered
Time complexity: the worst O(n!). At first step, you have n choice; the next step you have at most n-1 choice;
and so on. For each helper(), it takes O(n) to check if a queen can be put in a cell.
"""
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n : int
        :rtype  : List[List[str]]
        """
        res = []
        board = [ [0]*n for _ in xrange(n)]
        self.helper(n, 0, board, res)

        return res

    # recursively place a queen in all valid position in rth row
    # @param n: int, n-queens puzzle
    # @param r: int, find the valid position to put Q in rth row (index start with 0)
    # @param board: List[List[int]], the integer representation of board, where 0 and 1 indicate empty cell and queue separately
    # @param res  : final result set with distinguised complete solution
    def helper(self, n, r, board, res):
        #already put n queens, add current board into final result set
        if r >= n:
            sol = ["" for _ in xrange(n)]
            for i in xrange(n):
                for j in xrange(n):
                    sol[i] += "Q" if board[i][j]==1 else "."
            res.append(sol)
            return None

        for i in xrange(n):
            # no queue in ith column and 
            # no queue in the diagonal including board(r, i) from right to left
            # no queue in the diagonal including board(r, i) from left to right
            if (not any( board[j][i] == 1 for j in xrange(n))) and \
               (not any (board[r+j][i+j] for j in xrange(-min(r,i), min(n-r, n-i)))) and \
               (not any (board[r-j][i+j] for j in xrange(max(r-n+1, -i), min(r+1, n-i)))):
                #put queue in (r,i) cell
                board[r][i] = 1
                #recursively put the queue in next row
                self.helper(n, r+1, board, res)
                #restore the board from previous step
                board[r][i] = 0
        return None

        
