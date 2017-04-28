"""
In num array, all numbers appear three times except for one which appear only one time. Thus, if we view the numbers as bit representation, the count of each bit should be modular of 3 for all the number that appearred three times. If for one bit, the count is not modular of three, that bit is set in the single number.
For example, nums = [11,11,11,5]
    3: (1 0 1 1)
    3: (1 0 1 1)
    3: (1 0 1 1)
    1: (0 1 0 1)
    ------------
count: (3 1 3 4)

the sum of 3rd bit and 1st bit are not modular of 3, thus 3rd bit and 1st bit must be present in the singluar number, thus the singular number is 0101 = 5.

There are two methods to implement it.
1)A straigforward way. 
2)Use the truth table.
"""


"""
Method 1:
  A straigforward way. 
  Count the number of 1 in each bit and see if it is a modular of 3. To find out the number that appearred only 1 or 2 times, we only need to extract all bits that has counts%3 != 0
  For each number, we need to maximumly do bit operation for 32 times, since the longest integer can 32 bits. Thus, the time complexity is 32n, O(n)
"""
class Solution_2(object):
    _debug = 1

    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #return result
        r = 0

        #Initalize a 32 size array to count the 1s of each bit for each number in nums
        cnt = [ 0 for i in xrange(32)]

        #count 1s for each bit
        for num in nums:

            #ith bit
            i = 0
            while num: #while nums is not 0
                if num & 1: #if ith bit is 1
                    cnt[i] += 1
                num = num >> 1
                i += 1

        #loop through cnt, and find out the bits that are not modular of 3
        for i in xrange(32):
            if cnt[i] % 3 != 0:
                r |= 2**i # 2**i = 2 to the i, which will set the ith bit to 1

        return r

"""
Method 2:
    Use the truth table.
  Since there are only three states, num exist once, twice ane three times. We onl need two bits counter to represent all states (00, 01, 10). 

  Thus, the truth table for the state move is:

    current   incoming  next
    a b            c    a b
    0 0            0    0 0
    0 1            0    0 1
    1 0            0    1 0

    0 0            1    0 1
    0 1            1    1 0
    1 0            1    0 0

  => a = a&~b&~c + ~a&b&c  
     b = ~a&b&~c + ~a&~b&c
"""     
class Solution(object):
    _debug = 1 

    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        #a = a&~b&~c + ~a&b&c  
        #b = ~a&b&~c + ~a&~b&c
        a = 0 
        b = 0 
        for c in nums:
            na = a & ~b & ~c | ~a & b & c 
            nb = ~a & b & ~c | ~a & ~b & c 

            a, b = na, nb    

        #
        return a | b

"""
test
"""

myTest = Solution()
#testcase 1
print "-----------------------------"
print "tc1: nums = [1] => 1"
print myTest.singleNumber([1])

#testcase 1
print "-----------------------------"
print "tc1: nums = [3,3,3,1] => 1"
print myTest.singleNumber([3,3,3,1])
    
#testcase 2
print "-----------------------------"
print "tc2: nums = [3,4,4,1,3,4,3] => 1"
print myTest.singleNumber([3,4,4,1,3,4,3])
    
#testcase 3
print "-----------------------------"
print "tc3: nums = [11,5,11,11] => 5"
print myTest.singleNumber([11,5,11,11])

#testcase 4
print "-----------------------------"
print "tc4: nums = [-2,-2,1,1,-3,1,-3,-3,-4,-2] => -4"
print myTest.singleNumber([-2,-2,1,1,-3,1,-3,-3,-4,-2])

