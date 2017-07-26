class Solution2(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #sanity check
        if len(nums) == 0:
            return False

        #triplet
        triplet = [nums[0]]

        for i in xrange(1, len(nums)):
            if nums[i] <= triplet[-1]:
                if len(triplet) == 1 or nums[i] > triplet[-2]: 
                    triplet[-1] = nums[i]
                #else if nums[i] < triplet[-2], do not update triplet[-1]
            else: #nums[i] > triplet[-1]
                triplet.append(nums[i])
                print triplet
                if len(triplet) == 3:
                    return True

        return False

class Solution():
    def increasingTriplet(self,nums):
        res = [0,0,0]
        first = second = float('inf')
        for n in nums:
            if n <= first:
                first = n
                res[0] = n
            elif n <= second:
                second = n
                res[1] = n
            else:
                res[2] = n
                print res
                return True
        return False            

"""
test
"""
myTest = Solution()
print myTest.increasingTriplet([5,4,3,3,2,7,6,4,1,9])
print myTest.increasingTriplet([1,2,3,4,5])
print myTest.increasingTriplet([5,4,3,2,1])

         
