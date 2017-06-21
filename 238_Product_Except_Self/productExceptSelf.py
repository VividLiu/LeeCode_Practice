"""
Solution:
Initialize the output[] as all 1. When we iterate through nums array, accumulate the multiplication res by doing output[i] = output[i] * nums[j] (i != j)

Time complexity: O(n^2)
Space complexity: O(1)
"""
class Solution2(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype    : List[int]
        """

        #sanity check
        if len(nums) < 2:
            print "error: input nums does not contain enought number"
            return []

        #initialize return output
        output = [1] * len(nums)

        #iterate through nums while accumulateing multiplication result for each output[i]
        for i in xrange(len(nums)):
            for j in xrange(len(output)):
                if i != j:
                    output[j] *= nums[i]

        return output

        
"""
Solution:
Use two pass iteration
1) First pass from left to right and calculate the accumulated multiplication result except except itself.
    Thus, for nums[i], after first pass, tmp[i] contains accumulated mulitiplication result of nums[:i)
2) Second pass from right to pass and calculate the accumulated multiplication result except itself. 
    Thus, for nums[i], after second pass, tmp2[i] contains accumulated mulitiplication result of nums[i+1:]
3). Then output[i] = tmp1[i] * tmp2[i]

Time complexity: O(n)
Space complexity: O(1)
"""
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype    : List[int]
        """
        #sanity check
        if len(nums) < 2:
            print "error: nums array desn't have enough number"
            return []


        #initialize output array
        output = [1] * len(nums)

        acc = 1
        #first pass
        for i in xrange(len(nums)):
            output[i] = acc
            acc *= nums[i]

        acc = 1
        #second pass
        for i in xrange(len(nums)-1, -1, -1):
            output[i] *= acc
            acc *= nums[i]

        return output

