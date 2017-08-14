"""
Dynamic Programming
dp[i][j] = the edge length of maximum square with cell(i,j) as the right bottom corner.
if dp[i][j] = 1, then it can at least form a 1 unit square;
then if dp[i-1][j-1] >= 1 , it means there is a square ending at matrix[i-1][j-1];
if we can have a horizontal edge ending at matrix[i][j], and a vertical edge ending at matrix[i][j], 
we can combine the three neighbors and enlarge the size of dp[i-1][j-1] square.

Ex.
m = 
1, 1, 0
1, 1, 0
0, 0, 1

matrix[2][2] = 1, and also dp[1][1] = 2, but dp[2][2] can not form a larger square containing the square ending at matrix[1][1] since it doesn't have vertical edge and horizontal edge

m = 
1, 1, 0,
1, 1, 1,
1, 1, 1,

matrix[2][2] = 1, and also dp[1][1] = 2, but dp[2][2] only contains part of square ending at matrix[1][1] since it is contrained by the length of vertical edge which is 1
"""
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        
        #for r in xrange(len(matrix)):
        #    print matrix[r]
        
        #sanity check
        if len(matrix) == 0:
            return 0
        
        n, m = len(matrix), len(matrix[0])
        dp = [ [0] * m for _ in xrange(n)]
        
        #populate the first row and first column of dp array
        for i in xrange(n):
            dp[i][0] = 1 if matrix[i][0] == '1' else 0
        for j in xrange(m):
            dp[0][j] = 1 if matrix[0][j] == '1' else 0
            
        #popluate rest of dp array
        for i in xrange(1, n):
            for j in xrange(1, m):
                if matrix[i][j] == '1':
                    edge = dp[i-1][j-1]
                    #bug: can not use sum, because the 1 has to be continuous
                    #h_edge = sum(int(matrix[i][k]) for k in xrange(j-edge,j))
                    #v_edge = sum(int(matrix[k][j]) for k in xrange(i-edge, i))
                    
                    #to calculate the maximum size of horizontal edge ending at matrix[i][j]
                    h_edge = 0
                    for k in xrange(j-1, j-edge-1, -1):
                        if matrix[i][k] == '0':
                            break
                        else:
                            h_edge += 1
                    
                    #to calculate the maximum size of vertical edge ending at matrix[i][j]
                    v_edge = 0
                    for k in xrange(i-1, i-edge-1, -1):
                        if matrix[k][j] == '0':
                            break
                        else:
                            v_edge += 1
                    
                    #if h_edge <= edge and v_edge <= edge:
                    dp[i][j] = min(h_edge, v_edge, edge) + 1    
                    
                    #optimizaiotn:
                    #dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j])
        
        return max(max(row) for row in dp ) ** 2
                
"""
test
"""
myTest = Solution()
print myTest.maximalSquare(["10100","10111","11111","10010"])
print myTest.maximalSquare(["11100","11100","11111","01111","01111","01111"])
print myTest.maximalSquare(["0001","1101","1111","0111","0111"])
print myTest.maximalSquare(["0110111111111111110","1011111111111111111","1101111111110111111","1111111111111011111","1111111111111101111","1110111011111111101","1011111111111101111","1111111111111110110","0011111111111110111","1101111111011111111","1111111110111111111","0110111011111111111","1111011111111101111","1111111111111111111","1111111111111111111","1111111111111111101","1111111101101101111","1111110111111110111"])
