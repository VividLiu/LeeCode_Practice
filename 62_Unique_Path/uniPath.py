"""
Dynamic algorithm:

dp[i][j]: how many unique paths are there to reach grid[i][j].

Since the robot can only move down or right, thus,
    dp[i][j] = dp[i-1][j] + dp[i][j-1]
               if i != 0, j! = 0

dp[0][0] = 1
"""
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        #wrong way to create a two dimentional list to represent the grid
        # [0] * n, this syntax will reuse [0] list n times
        # [[0]*n] * m will resuse ([0]*n) m times
        # this will cause trouble when try to assign value to single cell
        #grid = [ [0] * n] * m

        #correct way to create the two dimentional array is
        grid =[[ 0 for x in xrange(n)] for y in xrange(m)]

        #initialize the start position number
        grid [0][0] = 1
        for i in xrange(m):
            for j in xrange(n):
                if i-1 >= 0 :
                    grid[i][j] += grid[i-1][j]
                if j-1 >= 0 :
                    grid[i][j] += grid[i][j-1]

                #print "------------"
                #print "i, j: " + str(i) + "," + str(j)
                #print grid

        return grid[m-1][n-1]

        
