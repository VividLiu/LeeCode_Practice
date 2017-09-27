"""
Dynamic programming:
The number of ways to change amount a using n kinds of coins equals
1) The number of ways to change amount a using all but the first
kind of coin. (don't use the first kind coin) 
plus
2) The number of ways to change a - d using all n kinds of coins, where d is the denomination of the first kind of coin. (Use the first kind of coin)

Define dp array 
dp[i, j+1]: use subset of coins[0:j], the number of ways to change amount i
dp[i, j+1] = dp[i, j] (1) + dp[i-coins[j], j+1] (2)

boundary case:
dp[0, j] = 1, there is always one way to change amount 0
dp[i, 0] = 0, the coins set is empty
"""
class Solution(object):
    def change(self, amount, coins):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """

        #initialize dp array
        dp = [[0] * (len(coins) + 1) for _ in xrange(amount+1)]

        for j in xrange (0, len(coins)+1):
            dp[0][j] = 1

        for i in xrange(1, len(dp)):
            for j in xrange(1, len(dp[0])):
                dp[i][j] = dp[i][j-1] + (dp[i-coins[j-1]][j] if i-coins[j-1] >= 0 else 0)   

        return dp[-1][-1]

"""
test
"""
myTest = Solution()
print myTest.change(5, []) 
print myTest.change(5, [1,2,5]) 
print myTest.change(100, [1,101,102, 103]) 





