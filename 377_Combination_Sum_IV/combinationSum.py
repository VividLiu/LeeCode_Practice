"""
Solution:
The straight forward solution: backtracking
Ex. nums = [1,2,3], target = 4
The expanded backtracking tree is:
          root
    /      |      \
   1       2       3 
 / | \   / |      / 
1  2  3 1  2     1  
|  |
1  1
|
1
"""
class Solution2(object):
    def combinationSum4(self, nums, target):
        """ 
        :type nums  : List[int]
        :type target: int
        :rtype      : int
        """
        res = [0] 

        self.bt(nums, target, 0, res)
    
        return res[0]

    #the backtracking helper function to calculate how many ways to get the sum as target
    # @param nums  : List[int], integers that can be used in the combination
    # @param target: int,       target sum
    # @param cursum: int,       current accumulating sum in this branch
    # @param res   : int,       the number ways accepted until current branch
    def bt(self, nums, target, cursum, res):
        if cursum > target: #reject
            return None
        elif cursum == target: #accept
            res[0] += 1
        else: #generating next level of candidates
            for x in nums:
                self.bt(nums, target, cursum+x, res)

        return None

"""
Solution: Dynamic Programming
Given a target t, and nums array, S(nums, t); how can we find the subproblem to construct the dp formula.
If we pick nums[i] as the first one in the combination to reach t, then the next subproblem would be S(nums, t-nums[i]).
Thus, S(nums, t) = sum( S(nums, t-nums[i]) where 0 <= i < len(nums) and nums[i] <= t)
"""
class Solution(object):
    def combinationSum4(self, nums, target):
        """ 
        :type nums  : List[int]
        :type target: int
        :rtype      : int
        """
        #initialzie dp array 
        dp = [0] * (target + 1)
        #edge case
        dp[0] = 1

        #fill the array bottom-up
        for i in xrange(1, len(dp)):
            dp[i] = sum( dp[i-nums[j]] for j in xrange(0, len(nums)) if nums[j] <= i)
        
        return dp[-1]
            
            

"""
test
"""
myTest = Solution()
print myTest.combinationSum4([1,2,3], 4)
print myTest.combinationSum4([1,3,5], 7)
        
