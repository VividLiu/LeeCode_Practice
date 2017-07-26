"""
Backtracking(Time limit exceeds)
Illustraction of the backtracking tree:
ex. nums = [ 1,1,1], S = 1. The node is the possible sum in nums[0:level]
              root
            /      \
           1        -1
         /  \      /   \
        2    0    0    -2 
       / \  / \  / \   / \
      3  1  1 -1 1 -1 -1  -3
"""
class Solution2(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """

        return self.bt(nums, 0, 0, S) 

    #backtracking helper function
    #@param nums    : List[int]
    #@param i       : +/-nums[i] is the number to be added to cur sum
    #@param cur     : current accumulating sum
    #@param target  : target sum
    #@return param  : int, the number of ways for target sum
    def bt(self, nums, i, cur, target):
        if i == len(nums):
            return 1 if cur == target else 0

        return self.bt(nums, i+1, cur + nums[i], target) + self.bt(nums, i+1, cur-nums[i], target)

"""
Backtracking with memorization.
From the above bactracking tree, we can see that there are a lot of redundant sub problems (i, s),
where i is index, s is current sum in nums[0:i]. 
Thus, we can use a map to store the intermediate result (i,s) to avoid redundant subproblems.
"""
class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums : List[int]
        :type S    : int
        :rtype     : int
        """
        cache = {}

        #closure function 
        #@param i     : int, nums array index
        #@param cur   : int, current sum using nums[0:i]   
        #@return param: int, the total number of ways for sum cur using nums[0:i]
        def helper(i, cur):
            if i == len(nums):
                return 1 if cur == 0 else 0
           
            if (i, cur) not in cache:
                #the number of ways to for (i, cur)
                s = helper(i+1, cur - nums[i]) + helper(i+1, cur+nums[i])    
                cache[(i, cur)] = s
        
            return cache[(i, cur)]

        return helper(0, S)

"""
Dynamic programming:
dp[i, j] means: the total number of ways to find sum j by assigning symbols for number in num[0:i]
dp[i, j] = dp[i-1, j-nums[i]] + dp[i-1, j+nums[j]]
ex. nums = [1,1,1], S = 1
range of sums of nums is -3 - 3
index:           0  1  2  3  4  5  6
mapped index:   -3 -2 -1  0  1  2  3   
             1   0  0  1  0  1  0  0  
             1   0  1  0  2  0  1  0
             1   1  0  3  0  3  0  0
"""
class Solution1(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums : List[int]
        :type S    : int
        :rtype     : int
        """
        #edge case
        if len(nums) == 0:
            return 1 if S == 0 else 0

        xmax = sum(nums)

        #sanity check
        if S > xmax or S < -xmax:
            return 0

        #initialize dp array
        dp = [ [0] *  (2 * xmax + 1) for _ in xrange(len(nums)) ] 

        for i in xrange(len(nums)):
            for j in xrange(2*xmax + 1):
                if i == 0:
                    #if nums[i] == 0, s = 0, there are two ways not one
                    dp[0][j] += 1 if nums[0] == j - xmax else 0 
                    dp[0][j] += 1 if nums[0] == -(j - xmax) else 0 
                else:
                    dp[i][j] += dp[i-1][j-nums[i]] if j-nums[i] >= 0 else 0
                    dp[i][j] += dp[i-1][j+nums[i]] if j+nums[i] < 2*xmax + 1  else 0

        return dp[-1][S + xmax]
        

"""
test
"""
myTest = Solution()
print myTest.findTargetSumWays([1,1,1,1,1], 3)
print myTest.findTargetSumWays([1,1,1,1,1], -3)
print myTest.findTargetSumWays([], 0)
print myTest.findTargetSumWays([], 1)
print myTest.findTargetSumWays([0,0], 1)
print myTest.findTargetSumWays([0,0], 0)
