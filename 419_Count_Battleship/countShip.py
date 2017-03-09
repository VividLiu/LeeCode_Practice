class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """

        #print board
        #print board[0]
        cnt = 0 
        for r in xrange(0, len(board)):
            for c in xrange(0, len(board[0])):
                #encounter the start of the battleship
                if board[r][c] == 'X' and (r-1 < 0 or board[r-1][c] == '.') and (c-1 < 0 or board[r][c-1] == '.'): 
                    cnt += 1;
    
        return cnt 

