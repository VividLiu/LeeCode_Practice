"""
Time limit Exceeds
"""
class Solution3(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        for i in xrange( x/2 + 1 + 1):
            if (i*i == x) or ( i*i < x and (i+1)*(i+1) > x):
                return i

"""
recursive binary search 
"""
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        #binary search for the root of x in inteveral of [low, high]
        def bSqrt(l, h):    
            if h == 1:
                return 1 
            
            if h - l <= 1: #h==l or l+1 = h
                return l
            
            m = (h+l)/2
            n = m*m 
            
            if n == x:
                return m
            elif n < x:
                return bSqrt(m, h)
            else:
                return bSqrt(l, m)
        
        return bSqrt(0, x)
            
"""
iterative binary search 
"""
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        #special case 
        if x == 1:
            return 1
        
        l, h = 0, x
        
        while l < h-1:
            m = (h+l)/2
            n = m*m
            
            if n == x:
                return m
            elif n < x:
                l = m
            else:
                h = m
            
        return l    
    

"""
test
"""
myTest = Solution()
print myTest.mySqrt(0)
print myTest.mySqrt(1)
print myTest.mySqrt(2)
print myTest.mySqrt(4)
print myTest.mySqrt(25)
print myTest.mySqrt(27)
print myTest.mySqrt(738379496)
