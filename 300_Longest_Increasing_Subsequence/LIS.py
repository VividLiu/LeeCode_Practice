"""
Dynamic Programming:
dp[i] means the length of longest increasing subsequence in subarray nums[0:i] which the sequence ends at nums[i]
dp[i] = max(dp[j] + 1) where j < i and nums[j] < nums[i]
or dp[i] = 1 if no such j exists
return max(dp)
Time complexity: O(n^2)
"""
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #sanity check
        if len(nums) == 0:
            return 0

        #initialize dp array
        #a single number is considered length 1 increasing subsequence
        dp = [1] * len(nums)

        for i in xrange(1, len(dp)):
            j = i - 1
            #max([] or [0]) is a way to special default list for max function when list is empty
            #in earlier version of python
            dp[i] += max( [dp[k] for k in xrange(0, j+1) if nums[k] < nums[i]] or [0])

        return max(dp)

"""
test
"""
myTest = Solution()
print myTest.lengthOfLIS([10, 9, 2, 5, 5, 7, 101, 18])
print myTest.lengthOfLIS([1,3,6,7,9,4,10,5,6])

