"""
Solution:
Using stack
"""
class Solution(object):
    #determine if the left character and right character can close.
    def erase(self, l,r ):
        if (l == '(' and r == ')') or (l == '{' and r == '}') or (l == '[' and r == ']'):
            return True
        else:
            return False
        
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        #edge case
        if s == "":
            return True
        
        stack = [s[0]]
        
        for i in xrange(1, len(s)):
            if stack:
                top = stack[-1]
                
                if self.erase(top, s[i]):
                    stack.pop()
                else:
                    stack.append(s[i])
            else:
                stack.append(s[i])
            
        
        return True if stack == [] else False

"""
test
"""
myTest = Solution()
print myTest.isValid("{[()]}")
print myTest.isValid("{[]}()")
print myTest.isValid("{[(])}")
