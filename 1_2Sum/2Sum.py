"""
Method 1:
    Use two 'for' loops to find all possible pairs and see if their sum equal to target.
    Time complexity: O(n^2), n is the size of nums 
"""
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        for i in xrange(len(nums)):
            for j in xrange(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

"""
Method 2:
    Use hash table.
    Iterate through nums array, and add (ni, i) into hash table where ni is ith number and i is index, then check if target-ni already exists in the hash keys, if it exist, it means there is another number nj in the array, which nj = target-ni
    Time complexity: O(n), n is the size of nums 
    Space complexity: O(n), n is the size of nums 
"""
class Solution(object):
    def twoSum(self, nums, target):
        hashTable = {}

        for i in xrange(len(nums)):
            if target - nums[i] in hashTable:
                j = hashTable[target-nums[i]]
                return [j, i]
            else:
                hashTable[nums[i]] = i

        return []
        

"""
myTest
"""
myTest = Solution()

#testcase 1):
print "-------------------------"
print "tc1: num = [], target = 1 ==> []" 
print myTest.twoSum([], 1)
            
#testcase 2):
print "-------------------------"
print "tc2: num = [1,0,-1], target = 0 ==> [0,2]" 
print myTest.twoSum([1,0,-1], 0)
         
#testcase 3):
print "-------------------------"
print "tc3: num = [2,7,11,15], target = 9 ==> [0,1]" 
print myTest.twoSum([2,7,11,15], 9)













