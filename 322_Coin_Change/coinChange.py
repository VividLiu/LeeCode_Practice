"""
Backtracking: (wrong answer)

Sort coins in descending order so we always pick the largest available coin
this will ensure that the first valid dfs branch is the answer

Note: this assumption isn't right.
ex. coin = [5, 4, 1], amount = 12
If we use above logic, the solution will be [5,5,1,1]; 
however the acutal shortest solution will be [4,4,4]
"""
class Solution2(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        #sort coins in descending order so we always pick the largest available coin
        #this will ensure that the first valid dfs branch is the answer
        coins.sort(reverse=True)
        
        def bt(rem, start, curres, res):
            print "bt: ", rem, start, curres
            #ending case:
            if rem == 0:
                res.append(curres)
                return True
            if rem < 0:
                return False
            
            #generating next level
            for i in xrange(start, len(coins)):
                
                if bt(rem-coins[i], i, curres + [coins[i]], res):
                    return True
            return False
        
        res = []
        
        if bt(amount, 0, [], res):
            print res
            return len(res[0])
        else:
            return -1

"""
Dyanamic programming (Time complexity exceeds)
"""
import sys
class Solution1(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """

        #initialize dp array
        dp = [[sys.maxint] * (len(coins) + 1) for _ in xrange(amount+1)]

        for j in xrange (0, len(coins)+1):
            dp[0][j] = 0

        for i in xrange(1, len(dp)):
            for j in xrange(1, len(dp[0])):
                dp[i][j] = min(dp[i][j-1] , 1+(dp[i-coins[j-1]][j] if i-coins[j-1] >= 0 else sys.maxint))

        return dp[-1][-1] if dp[-1][-1] != sys.maxint else -1

"""
Dynamic proggramming:
f V == 0, then 0 coins required.
If V > 0
   minCoin(coins[0..m-1], V) = min {1 + minCoins(V-coin[i])} 
                               where i varies from 0 to m-1 
                               and coin[i] <= V
"""
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        #initialize dp
        dp = [ sys.maxint ] * (amount+1)
        dp[0] = 0

        #
        for i in xrange(1, len(dp)):
            #print dp
            dp[i] = min( dp[i - c]  if i - c >= 0 else sys.maxint for c in coins)
            if dp[i] != sys.maxint:
                dp[i] += 1

        print dp
        return dp[-1] if dp[-1] != sys.maxint else -1

"""
test
"""
myTest = Solution()
print myTest.coinChange([1,2,5], 11)
print myTest.coinChange([2], 3)

