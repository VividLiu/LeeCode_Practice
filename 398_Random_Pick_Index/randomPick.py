"""
The most straight forward way is:
Iterate through the nums list, and find all the numbers which is equal to target, record their index in an extra list and randomly pick one.
The problem is if there are a lot of numbers in nums that are equal to target, it will cause a lot of extra memory 
"""
class Solution2(object):

    def __init__(self, nums):
        """
        
        :type nums: List[int]
        :type numsSize: int
        """
        self._nums = nums
        

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        return random.choice([k for k, v in enumerate(self._nums) if v == target])

"""
Solution: Reservoir Sampling
Reference for Reservoir Sampling:
http://www.geeksforgeeks.org/reservoir-sampling/
https://en.wikipedia.org/wiki/Reservoir_sampling
"""
class Solution(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        :type numsSize: int
        """
        self._nums = nums
        
    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        picked = -1
        cnt = 0 #how many target values we have encountered so far
        for i, x in enumerate(self._nums):
            if x == target:
                cnt += 1
                r = random.randint(1, cnt)
                #as long as the possiblity to choose this number is 1/cnt
                if r == 1:
                    picked = i

        return picked


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
