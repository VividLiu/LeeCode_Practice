"""
Method:
    Similar to 1.Two Sum.
    Use hash table to store (-nk, k) where k = 0..n-1.
    Then use two 'for' loops to get a pair of (ni, nj), if ni + nj exist in hash, it means there is some -nk exist where ni+nj=-nk => ni+nj+nk=0
    However, the process above will find all triples, also the duplicates since nums array can have duplicates.
    Time complexity: O(n^2), n is the size of nums
    Space complexity: O(n), n is the size of nums
"""
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #return result
        res = []

        #sort the array first
        nums.sort()

        #populate the hashtable
        hashTable = {}

        for k in xrange(len(nums)):
            #hashTable.setdefault(-nums[k], []).append(k)
            #store the maximun index for the same value
            hashTable[-nums[k]] = k
           
        #iterate
        for i in xrange(len(nums)):
            #skip the same element to avoid generating duplicates
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in xrange(i+1, len(nums)):
                #skip the same element to avoid generating duplicates
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                if (nums[i] + nums[j]) in hashTable:
                    k = hashTable[nums[i]+nums[j]]
                    if k > j:
                        res.append([nums[i], nums[j], nums[k]])
                    """
                    for k in hashTable[nums[i]+nums[j]]:
                        if k > j:
                            res.append([nums[i], nums[j], nums[k]])
                            break
                    """
        return res

"""
myTest
"""
myTest = Solution()

#testcase 1:
print "------------------------------"
print "tc1: nums = [-1, 0, 1, 2, -1, -4]] ==> [ [-1, 0, 1], [-1,-1,2] ]"
print myTest.threeSum([-1, 0, 1, 2, -1, -4])

#testcase 2:
print "------------------------------"
print "tc2: nums = [-1, 0, 1, 2, -1, -4, 1, 0, 1, 2] ==> [[-4,2,2], [-1,0,1],[-1,-1,2]]"
print myTest.threeSum([-1, 0, 1, 2, -1, -4, 1, 0, 1, 2])


