"""
Basically, the proble asks to find the biggest difference of prices[j] - prices[i] where i <= j.
Thus, we can construct a minPrices array, which minPrices[i]a means the minimal number from prices[0:i] (i inclusively).
And the result will be max(prices[i] - minPrices[i])
Time complexity: O(n), Space comlexity: O(n)

improvement:
Use two pointer solution
We don't need create an additional minPrices array, just use a pointer to indicate the smallest price index
Time complexity: O(n), Space complexity: O(1)

"""
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        #sanity check:
        if len(prices) == 0:
            return 0
        
        #construct min prices array
        minPrices = [0] * len(prices)
        for i in xrange(len(prices)):
            minPrices[i] = min(minPrices[i-1], prices[i]) if i > 0 else prices[0]
        
        maxProfit = 0
        for i in xrange(len(prices)):
            maxProfit = max(maxProfit, prices[i] - minPrices[i])
        
        return maxProfit
    
class Solution2(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        #sanity check
        if len(prices) == 0:
            return 0
        
        minPrice, maxProfit = prices[0], 0
        
        for i in xrange(len(prices)):
            if prices[i] < minPrice:
                minPrice = prices[i]
            
            maxProfit = max(maxProfit, prices[i] - minPrice)
        
        return maxProfit
            
        
