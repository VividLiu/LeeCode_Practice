class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(findNums) == 0 or len(nums) == 0:
            return []
            
        stack = [nums[0]]
        lookup = {}
        result = []

        for num in nums[1:]:

            #pop all the elements that are smaller than the current num and set their next greater as current num
            while(len(stack) != 0 and stack[-1] < num):
                m = stack.pop()
                #set the next greater number for m in lookup dictionary
                lookup[m] = num 

            #push the current number in stack
            stack.append(num)
    
        #if there are remaing nums in stack, set their next greater to be -1
        while(len(stack) != 0): 
            m = stack.pop()
            lookup[m] = -1  

        #debug
        #print lookup

        #
        for num in findNums:
            result.append(lookup[num])

        return result
