"""
Backtracking.
The difference between combination sum II and I is that II allows duplicates in the number array; and each number element can be used once in each combination.
Thus, when backtracking, the next level start from i+1 instead i in I.
And we need sort the nums first and skip the duplicates if it is not start
"""
class Solution(object):
    def combinationSum2(self, prices, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        #sort prices array first
        prices.sort()

        #define backtracking recursive function
        #param remain: int, remaining sum
        #param ind   : int, index of the element being taken
        #param res   : List, current result set
        #param res   : List[list], total result set
        def bt(remain, ind, curres, res):
            #acceptance case
            if remain - prices[ind] == 0 and curres + [prices[ind]] not in res:
                res += [ curres + [prices[ind]]]
                return None
            #rejection case
            if remain - prices[ind] < 0 or ind == len(prices):
                return None

            #generate next steps
            for i in xrange(ind+1, len(prices)):
                bt(remain-prices[ind], i, curres+[prices[ind]], res)
            return None

        res = []
        for i, p in enumerate(sorted(prices)):
            bt(target, i, [], res)

        return res 
        
"""
test
"""
myTest = Solution()
print myTest.combinationSum2([10,1,2,7,6,1,5], 8)
