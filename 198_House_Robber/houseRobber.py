"""
One observation is that the robber either skip one or two houses between the robbed houses.
If he skips three in a row, he can always rob the middle one among the three without alerting the alarm. Thus, he will mostly skip two houses in a row. 

Dynamic programming
Keep two extra list with the same length of houses list.
One array s1, s1[i] means the maximum money he can rob without taken ith house.
Another array s2, s2[i] means the maximum money he can rob takenith house.
Thus,
s1[i] = max(s1[i-1], s2[i-1])
s2[i] = s1[i-1] + house[i]
The result is max(s1[-1], s2[-1]
"""

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        #s1[i]: not taken ith; s2[i]: taken ith
        s1, s2 = [0] * len(nums), [0] * len(nums)
        s1[0], s2[0] = 0, nums[0]

        for i in xrange(1, len(nums)):
            s1[i] = max(s1[i-1], s2[i-1])
            s2[i] = s1[i-1] + nums[i] 
         
        return max(s1[-1], s2[-1])

"""
Optimization:
Instead of using two extra list, we only need to use two extra varaible to store s1[i-1], s2[i-1]
"""
class Solution2(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        #rob: the maximum money can get if rob current house
        #norob: the maximum money can get if not rob current house
        rob, norob = nums[0], 0

        for i in xrange(1, len(nums)):
            tmp = norob + nums[i]
            norob = max(rob,norob)
            rob = tmp

        return max(rob, norob)




