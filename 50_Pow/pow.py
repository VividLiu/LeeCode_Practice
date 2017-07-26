"""
Time complexity: O(logn)
"""
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """

        #edge case
        if n < 0:
            return 1.0/self.myPow(x, -n)
        if n == 0:
            return float(1)
        if n == 1:
            return x
        if n == 2:
            return x * x

        #already make sure that n > 0
        if n % 2 == 0: #n is even
            return self.myPow(self.myPow(x, n/2), 2)
        else: #n is odd
            return x * self.myPow(x, n-1)
        
"""
test
"""
myTest = Solution()
print myTest.myPow(5, 12)
print myTest.myPow(5, 13)
print myTest.myPow(5, -2)
