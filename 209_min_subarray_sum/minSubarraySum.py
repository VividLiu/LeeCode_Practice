"""
Two pointer solution:
The first loop to advance j, when sum(nums[i:j+1]) >= s,
go to the inner loop to shrink [i:j+1] window, which is advance i until
sum[i':j+1] is not >= s anymore. 
Then go back to first loop to advance j to look for next valid substring
"""
class Solution2(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        
        #sanity check:
        if len(nums) == 0:
            return 0
        
        i, j = 0, 0
        I, J = 0, 0
        
        curSum = 0
        
        #advance j
        for j, num in enumerate(nums, 1):
            curSum += num
            
            #print "---"
            #print "i, j: ", i, j,
            #print "curSum: ", curSum
            
            while curSum >= s and i < j:
                if not J or j - i < J - I:
                    I, J = i, j
                    #print "    update I, J: ", I, J
                
                #advance i
                curSum -= nums[i]
                i += 1
                
        return J-I
    
"""
Binary search solution
First, build an array with the running sum from element -1 to n-1
we set sums[0] so sums[1] can be sum of nums[0], and be consistent with rest sums[j]
sums[j]: sum of nums[0] to nums[j-1] where j>=1
ex. [2,3,1,2,4,3] => [0, 2, 5, 6, 8, 12, 15] 
If sums[j] - sums[i] >= s (j>=1), we know sum of nums[i]: nums[j-1] >=s.
Thus nums[i:]: nums[j-1] is a valid sub array.
In other words, sums[i] + s <= s[j].
We will have an iteration through sums for i, and to search if such s[j] exist, we can build a binary search tree, so the search time will be O(logn)
ex.        6
         /   \
        2     12
       / \   /  \
      0   5 8    15
This search only works for positive num array, so if sums[j] > sum[i] => j > i.
If the array has negative numbers, sums[j] > sums[i] is no guarantee for j > i
Time complexity: O(nlogn)
"""

class Solution(object):
    _debug = 1
    
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        
        #sanity check:
        if len(nums) == 0:
            return 0
        
        if s == 0:
            return 1
        
        #construct running sum array, with sums[0] is initialed as 0
        sums = reduce(lambda x, y: x + [x[-1] + y], nums, [0])
        
        if self._debug:
            print "sums: ", sums
        
        #the variable to denote the start and end (exclusively) index of the minimum valid subarray
        I, J = 0, 0
        
        #for each sums[i], find the j which sum[j] has the smallest, but >= sums[i]+s value
        for i in xrange(len(sums)):
            target = sums[i] + s
            
            #search binary tree
            #s can be 0, thus, search from i inclusively
            if self._debug:
                print "search interval: ", i, len(sums)-1
            
            j = self.bSearch(sums, i, len(sums)-1, target)
            
            if self._debug:
                print "search result: ", j
            
            if j != -1 and (not J or j - i <= J - I):
                J, I = j, i
                
                if self._debug:
                    print "record ", I, J    
        
        return J-I
     
    #search for the smallest index I, which nums[I] >= target
    def bSearch(self, nums, l, h, target):
        """
        :type nums : List[int]
        :type l    : int, the pointer of start position of current search interval
        :type h    : int, the pointer of end position inclusively of current search interval
        :target    : int, target value to be searched
        :rtype     : int, the found index, return -1 if nothing found
        """
        
        while l <= h:
            if self._debug:
                print "    new search: ", l, h, "with target=",target
            
            #edge case:
            #len(interval) == 1:
            if h == l:
                return l if nums[l] >= target else -1
            #len(interval) == 2:
            if h - l == 1:
                #if nums[l] > target:
                #next search interval will be empty array
                if nums[l] >= target:
                    return l
                #if nums[l] < target:
                #continue search in [mid, h] which is nums[h] interval
            
            mid = l + (h-l)/2    
            
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                h = mid-1
                
                #next search interval will be nums[l:h]
                #if nums[h] < targt, mid will be the smallest index where nums[mid] >= target
                if nums[h] < target:
                    return mid    
            else: 
                l = mid+1
                
        return -1       
        
"""
myTest
"""

myTest = Solution()

"""
print "-------------------------"
print "tc1: nums=[], s=0 => 0 ([])"
print myTest.minSubArrayLen(0, [])

print "-------------------------"
print "tc2: nums=[1,2,3], s=0 => 1 "
print myTest.minSubArrayLen(0, [1,2,3])

print "-------------------------"
print "tc3: nums=[2,3,1,2,4,3], s=7 => 2 ([4,3])"
print myTest.minSubArrayLen(7, [2,3,1,2,4,3])

print "-------------------------"
print "tc4: nums=[1,2,3,4,5,0,0], s=11 => 5 ([3,4,5])"
print myTest.minSubArrayLen(11, [1,2,3,4,5,0,0])

print "-------------------------"
print "tc5: nums=[1,1,1,2,5,1,1], s=7 => 2 ([2,5])"
print myTest.minSubArrayLen(7, [1,1,1,2,5,1,1])

print "-------------------------"
print "tc6: nums=[1,1,1,2,5], s=12 => 0 ([])"
print myTest.minSubArrayLen(12, [1,1,1,2,5])

print "-------------------------"
print "tc7: nums=[1,1,1,1,5], s=5 => 1 ([5])"
print myTest.minSubArrayLen(5, [1,1,1,1,5])

print "-------------------------"
print "tc8: nums=, s=213 => 8 "
print myTest.minSubArrayLen(213,[12,28,83,4,25,26,25,2,25,25,25,12] )
"""
