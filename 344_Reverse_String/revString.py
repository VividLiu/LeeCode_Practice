import math

class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        n = len(s) #length of string
        slist = list(s) #split string into list object
        i = 0
        
        while( i  < math.floor(n/2)):
            swap = slist[i]
            slist[i] = slist[n-1-i]
            slist[n-1-i] = swap
            
            i += 1
        
        return ''.join(slist)

"""
test
"""
myTest = Solution();
print myTest.reverseString("wo shi yi ge xiao xiao liao"); 
