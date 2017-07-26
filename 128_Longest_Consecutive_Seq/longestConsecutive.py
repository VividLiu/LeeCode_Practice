"""
"""
class Solution2(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype    : int
        """
        
        #remove duplicats
        nums = list(set(nums))

        #
        dictSet = {}
        
        for x in nums:
            if x-1 in dictSet:
                tmp = dictSet.pop(x-1)
                tmp.append(x)
                dictSet[x] = tmp
            else:
                dictSet[x] = [x]

        print "first dict:"
        print dictSet

        for k in dictSet:
            preend = k - len(dictSet[k])
            if preend in dictSet:
                tmp = dictSet[preend]
                dictSet[k] = tmp + dictSet[k]

        print "second dict:"
        print dictSet

        key, maxlength = 0, 0
        for k in dictSet:
            if len(dictSet[k]) > maxlength:
                key, maxlength = k, len(dictSet[k])

        print "the key and length:"
        print key

        return maxlength 
"""
Solution:
First turn the nums list to a set (this also handles duplicates since it will eliminate duplicates when turned into set)

"""
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype    : int
        """

        numset = set(nums)
        maxl = 0

        while numset:
            x = numset.pop()
            l = 1

            #check left side of x
            lx = x-1
            while lx in numset:
                numset.remove(lx)
                l  += 1
                lx -= 1

            #check right side of x
            rx = x + 1                              
            while rx in numset:
                numset.remove(rx)
                l  += 1
                rx += 1

            maxl = l if l > maxl else maxl

        return maxl

    
"""
test
"""
myTest = Solution()
print myTest.longestConsecutive([8, 9, 12, 5, 6, 7])
print myTest.longestConsecutive([100, 4, 200, 1, 3, 2])
print myTest.longestConsecutive([1, 2, 0, 1])
print myTest.longestConsecutive([4,0,-4,-2,2,5,2,0,-8,-8,-8,-8,-1,7,4,5,5,-4,6,6,-3])
 
        
         
        
