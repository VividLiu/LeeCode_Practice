"""
Solution:
Depends on the choice of pivot, the array is partitioned to two parts.
nums[0:p] will be numbers >= pivot, nums[p+1:] will be numbers < pivot.
Given a target t, if t >= nums[0], then search t in nums[0:p]; if t < nums[0], then search t in nums[p+1:] backwards.

Depends on the choice of pivot, the time complexity varies.
Time complexity: worst O(n).
"""
class Solution2(object):
    def search(self,  nums, target):
        """ 
        :type nums  : List[int]
        :type target: int
        :rtype      : int
        """ 

        #sanity check
        if len(nums) == 0:
            return -1

        if target == nums[0]:
            return 0
        elif target > nums[0]:
            i = 1
            while i < len(nums) and nums[i-1] < nums[i]:
                if target == nums[i]:
                    return i
                i += 1
            return -1
        else: #target < nums:
            i = len(nums)-1
            while i >= 0  and (i == len(nums)-1 or nums[i] < nums[i+1]):    
                if target == nums[i]:
                    return i
                i -= 1
            return -1

"""
Solution: Binary search
Since the array is rotated in some pivot, it is not a fully sorted array, so we can not use the normal binary search. 
But the array is partially sorted since it is partitioned to two part by the pivot(nums[0]. nums[0: i] will be all numbers >= pivot in ascending order; nums[i+1:] will be all numbers < pivot in ascending order
To do binary search in this special array, let's consider all the possible situtaions where nums[mid] and target fall into the array, and decide its correspondind search halves.

1). if nums[mid] is in the same side with nums[0]: 
    a. if target < nums[mid] and target is in same side with nums[mid]
        search in [low, mid-1] half
    b. if other than condition of a which are target > nums[mid] or (target < nums[mid] but they are in different side)
        search in [mid+1, high] half
2). if nums[mid] is in different side with nums[0]:
    a. if target > nums[mid] and target is in same side with nums[mid]         
        search in [mid+1, high] half
    b. if other than condation of a which are target < nums[mid] or (target > nums[mid] but they are in different die):
        search in [low, mid-1]

"""
class Solution(object):
    def search(self, nums, target):
        """
        :type nums  : List[int]
        :type target: int
        :rtype      : int
        """
        #sanity check
        if len(nums) == 0:
            return -1

        low, high = 0, len(nums)-1

        #binary search iteration
        while low <= high:
            mid = low + (high-low) / 2 
    
            if target == nums[mid]:
                return mid
            elif ( ((nums[mid] - nums[0] >= 0) == (target - nums[0] >= 0)) and target < nums[mid]) \
                    or ( ((nums[mid] - nums[0] >= 0) != (target - nums[0] >= 0))  and target > nums[mid]):
                high = mid - 1
            else:
                low  = mid + 1

        return -1








