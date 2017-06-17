"""
Backtracking to list all the possible subsets.
"""
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        subsets = [[]]
        
        #to construct subset, for each number in nums, it is either in one subset or not
        for i, num in enumerate(nums):
            newsets = []
            for subset in subsets:
                newsets.append(subset[:] + [num])
            subsets.extend(newsets)
        
        return subsets

"""
test
"""
myTest = Solution()
print myTest.subsets([])
print myTest.subsets([1,2,3])
        
