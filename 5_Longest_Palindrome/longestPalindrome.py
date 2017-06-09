"""
Two pointer solution:
Outer loop to advance the pointer ctr which server as the center point of the palindrome string. 
Ex. dabad, b is the center point
    abba, bb are the center points
And the inner loop to compare the the characters at left and right side of center pointer.
"""
class Solution2(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        #sanity check
        if len(s) == 0:
            return ""
        
        if len(s) == 1:
            return s[0]
        
        #the start and end index of the longest palindromic substring
        I, J= 0,-1
        
        for ctr in xrange(0, len(s)-1):
            
            #s[ctr] as center point, propogate the search from center to left and right end
            #ex. aba, b as center
            i = ctr
            j = ctr
            
            while i >= 0 and j < len(s) and s[i] == s[j]:
                if j - i >= J - I:
                    J, I = j, i
                
                i -= 1
                j += 1
                
            #s[ctr:ctr+1] inclusively, as center, propograte the earch to both ends
            #ex. abba, bb as center
            if s[ctr] == s[ctr+1]:
                if J - I <= 1:
                    J, I = ctr+1, ctr     
                    
                i = ctr - 1
                j = ctr + 2
                
                while i >= 0 and j < len(s) and s[i] == s[j]:
                    if j - i > J - I:
                        J, I = j, i
                    
                    i -= 1
                    j += 1
        
        return s[I:J+1]
         
"""
Dynamic programming
dp[i][j] = 1 if s[i:j] inclusively can form a palidromic string
             since j >= i, only need to fill the up-left half table
Edge case: 
dp[i][i]   = 1, since single characater 'x' is a palindromic string
dp[i][i+1] = 1, if s[i] == s[i+1]. ex. 'bb'

recursion formula:
dp[i][j] = dp[i+1][j-1] if i > 0 and j > 0 and j-1>=i+1 and s[i] == s[j] 

Time complexity: O(n^2)
Space complexity: O(n^2)
"""
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        #sanity check
        if len(s) == 0:
            return ""
         
        n = len(s) #length of s string
        I, J = 0, 0 #the i, j index of longest palindromic string
        
        #initialize dp array
        dp = [ [0] * n for _ in xrange(n)]
        
        #set dp[i][i] and dp[i][i+1]
        for i in xrange(n):
            dp[i][i] = 1
            
            if i < n-1 and s[i] == s[i+1]:
                dp[i][i+1] = 1
                
                I, J = i, i+1 
        
        
        #fill the rest of dp array in order of from 
        for l in xrange(2, n+1): #length of substring
            for i in xrange(n-1): #start index of substring
                j = i+l-1
                if j < n and s[i] == s[j] and dp[i+1][j-1] == 1:
                    
                    dp[i][j] = 1
                    
                    if j - i > J - I:
                        I, J = i, j
                        
                        
        return s[I:J+1]
        
"""
test
"""
myTest = Solution()

print "----------------------"
print "tc1: s = '' ==> ''"
print myTest.longestPalindrome('')

print "----------------------"
print "tc2: s = 'babad' ==> 'bab'"
print myTest.longestPalindrome('babad')

print "----------------------"
print "tc3: s = 'ghbabadefhg' ==> 'bab'"
print myTest.longestPalindrome('ghbabadefhg')

print "----------------------"
print "tc4: s = 'ghbacfdefhg' ==> 'g'"
print myTest.longestPalindrome('ghbacfdefhg')

print "----------------------"
print "tc5: s = 'bb' ==> 'bb'"
print myTest.longestPalindrome('bb')

print "----------------------"
print "tc6: s = 'bbbbb' ==> 'bbbbb'"
print myTest.longestPalindrome('bbbbb')
