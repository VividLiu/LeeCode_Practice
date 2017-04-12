"""
Solution:
Use bit manipulation.
1). Use bit operator XOR (exclusive or) to cancel out the same numbers since XOR same bits will result in bit 0.
2). Need to separate out the two numbers (denote as a1, a2) into two different groups so that when we do XOR again in each group, the result will be the number itself. 
    Since we already got the XOR result of a1 and a2 in the first step (ex. r = a1 XOR a2), we must be able to find at least one bit in r that is set to 1 since a1 and a2 are different, thus at least one bit is differnt, then the result of XOR that bit will be 1. All the rest numbers in array must fall into either one group, with that bit set or unset. Thus we are able to separte the array into two groups with a1, a2 are guaranteed to be in different groups.
"""
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype:     List[int]
        """

        #xor all numbers will lead to the result of xor those two different numbers since the same numbers will cancel each other with xor operation
        r = reduce(lambda x, y: x ^ y, nums)

        #find the rightmost bit which is set to 1
        #use 1 which has the lowest set as inital mask, if r&mask == 0, the lowest bit in r is 0. Then left shift the masking bit in mask until it find the rightmost bit set in r
        mask = 1
        while (r & mask == 0):
            mask = mask << 1

        #improvement:
        #mask = r & ~(r-1)

        #initialize two groups with 0
        #Since n xor 0 => n, (n xor n => 0)
        g1, g2 = 0, 0

        #use the mask to separate all numbers into two groups
        #one group with masking bit set, another one with masking bit unset
        for x in nums:
            if x & mask == 0: #masking bit unset in this number, categorized as group 1
                g1 ^= x
            else: #masking bit set in this number, categorized as group 2
                g2 ^= x

        return [g1, g2]

"""
test
"""

myTest = Solution()

#testcases
print "testcase: [2, 3]"
print myTest.singleNumber([ 2, 3]) #no same number

print "testcase: [1, 2, 3, 1]"
print myTest.singleNumber([ 1, 2, 3, 1]) # one same number

print "testcase: [1, 2, 3, 4, 5, 2, 3, 4]"
print myTest.singleNumber([ 1, 2, 3, 4, 5, 2, 3, 4]) #multiple same number

print "testcase: [1, -2, 3, 4, 5, -2, 3, 4]"
print myTest.singleNumber([ 1, -2, 3, 4, 5, -2, 3, 4])#has negative nums

print "testcase: [-1, -2, 3, 4, 5, -2, 3, 4]"
print myTest.singleNumber([ -1, -2, 3, 4, 5, -2, 3, 4])#has negative nums

print "testcase: [-1, -2, 3, 4, -5, -2, 3, 4]"
print myTest.singleNumber([ -1, -2, 3, 4, -5, -2, 3, 4])#has negative nums
