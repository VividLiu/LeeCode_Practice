"""
"""
class Solution(object):
    _symbol = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        #sanity check:
        if s == "":
            print "error: empty roman string"
            return None

        res = 0
        for i in xrange(len(s)):
            if i < len(s)-1 and self._symbol[s[i]] < self._symbol[s[i+1]]:
                res += -self._symbol[s[i]]
            else:
                res += self._symbol[s[i]]

        return res

"""
test
"""
myTest = Solution()
print myTest.romanToInt("MCMLIV")    
print myTest.romanToInt("MMXIV")    
print myTest.romanToInt("MCMXC")    
