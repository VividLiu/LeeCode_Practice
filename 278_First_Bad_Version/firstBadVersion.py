from random import randint
import math
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

"""
Binary Search
"""
class Solution2(object):
    _debug = 0
    #_versions = []

    def isBadVersion(self, v):
        if v == 1:
            return True
        else:
             return False

    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        #self._versions = n    

        #start and end index of binary search subarray
        s = 0
        e = len(n) - 1
        m = 0    

        while s != e:
            m = int(math.ceil( (e-s+1)/2.0)) - 1 + s

            if self._debug:
                print "s=" + str(s) + ", e=" + str(e) + ", m=" + str(m)

            if self.isBadVersion(n[m]):#middle one is bad, move end pointer to the middle
                if self._debug:
                    print "     m is bad"
                e = m
            else: #middle one is good, move start pionter to the one after mid
                if self._debug:
                    print "     m is good"
                s = m+1

        if self.isBadVersion(n[s]):
            return s
        else:
            return -1

class Solution(object):
    def isBadVersion(self, v):
        if v == 1:
            return True
        else:
             return False

    def firstBadVersion(self,n):
        if self.isBadVersion(n[0]):
            return 0
        elif (not self.isBadVersion(n[-1])):
            return -1
        else:
            return self.firstBadIndex(n, 0, len(n)-1)

    def firstBadIndex(self, items, goodIndex, badIndex):
        if (badIndex - goodIndex) <= 1:
            return badIndex 

        nextIndex = int(math.ceil((badIndex - goodIndex)/2.0))

        if self.isBadVersion(items[nextIndex]):
            badIndex = nextIndex
        else:
            goodIndex = nextIndex
        
        return self.firstBadIndex(items, goodIndex, badIndex)
"""
test
""" 
myTest = Solution()

#assume 1 means bad, 0 means good for test convenience
#testcase 1):
print "---------------------------------"
print "tc1: n = [0] ==> -1"
print myTest.firstBadVersion([0])

print "---------------------------------"
print "tc2: n = [0,0] ==> -1"
print myTest.firstBadVersion([0,0])

print "---------------------------------"
print "tc3: n = [0,1] ==> 1"
print myTest.firstBadVersion([0,1])

print "---------------------------------"
print "tc4: n = [0,0,1] ==> 2"
print myTest.firstBadVersion([0, 0, 1])

print "---------------------------------"
print "tc5: n = [1,1,1,1] ==> 0"
print myTest.firstBadVersion([1, 1, 1, 1])

print "---------------------------------"
print "tc6: n = [1,1,1,1,1] ==> 0"
print myTest.firstBadVersion([1,1,1,1,1])

print "---------------------------------"
print "tc7: n = [0,0,1,1,1] ==> 2"
print myTest.firstBadVersion([0,0,1,1,1])
