"""
Method 2 & 3:
Use recursion.
For a string s0s1s2s3s4s5...sN-1, if we know the number of decode ways for substring s[1:N] and s[2:N], denoted as d[1:N] and d[2:N], then
d[0:N] = d[1:N]
         + d[2:N] if s0s1 can be decoded (which is int(s0s1) < 27 and s0 is not 0)

Ex. s =  '2123'
         /    \
   2 (123)    21 (23)
       / \
 1 (23)  12 (3)

'23': there are two ways to decode; '3': there is only one way to decode; thus the number of ways to decode '123' is 2+1=3
similary, there is three ways to decode '123', two ways to decode '23', thus the number of ways to decode '2123' is 3+2 = 5 

However a problem of above formular didn't consider the impact of illegal 0s.
Thus method 3 preprocess the string to check if it contains illegal 0s first to determine if the string can be coded or not. while method 2 does the checking along the recursive process.

"""
class Solution3(object):
    def numDecodings(self, s):
        """ 
        :type s: str
        :rtype: int
        """

        #special case, if 0 is the first character or appears after 
        #after anything other than 1 or 2, there is no way to decode the string
        for i in xrange(len(s)):
            if s[i] == '0' and (i == 0 or s[i-1] not in ['1','2']):
                return 0

        return self.helper(s)

    #recursive helper function
    def helper(self, s):
        #edge case
        if len(s) == 0:
            return 0
        if s[0] == '0':
            return 0
        if len(s) == 1:
            return 1

        if int(s[0:2]) < 27:
            return self.helper(s[1:]) + (self.helper(s[2:]) if len(s) > 2 else 1)
        else:
            return self.helper(s[1:])
        #return self.numDecodings(s[1:]) + (self.numDecodings(s[2:]) if int(s[0:2]) < 27 else 0)

class Solution2(object):
    def __init__(self):
        self.flag = True #flag if current string s can be coded

    def numDecodings(self, s):
        """ 
        :type s: str
        :rtype: int
        """

        #reset the flag to True
        self.flag = True

        num = self.helper(s)
    
        if self.flag:
            return num
        else:
            return 0

    def helper(self, s):
        #edge case:
        if len(s) == 0:
            return 0
        if s[0] == '0':
            return 0
        if len(s) == 1:
            return 1  

        #find the end of continuous 0s from second character if any
        #and record that position
        i, p = 1, 0
        while i < len(s) and s[i] == '0':
            p += 1  
            i += 1

        #it means there are more than one coninuous '0's, since single one can not be decodes, this string can not be decoded
        if p > 1: 
            self.flag = False
            return 0

        if int(s[0:2]) < 27:
            return self.helper(s[1:]) + (self.helper(s[2:]) if len(s) > 2 else 1)
        elif s[1] == '0': # since s[0:2] < 27, it means s[0:2] must be '30', '40'...'90' which can not be decoded
            self.flag = False
            return 0
        else:
            return self.helper(s[1:])

"""
Use dynamic programing.
Both above solutions use recursive which will result in 'Exceed time limit'.
dp[i]: the number of ways to decode s[0 -> i] (i inclusively)
dp[0] = 1 if dp[0] is not '0' because there is no way to decode singlular '0'
dp[i] =  dp[i-1] if s[i] != 0 ( if we can decode singular s[i], we can simply append it to all previous decoded strings, and the new decoded strings will still be valide)
      = + dp[i-2] if s[i-2]s[i-1] can be decoded. 
"""
class Solution(object):
    def numDecodings(self, s): 
        """ 
        :type s: str
        :rtype: int
        """
    
        #edge case        
        if len(s) == 0 or s[0] == '0':
            return 0 

        #initialize dp array
        dp = [ 0 for i in xrange(len(s))] 
        dp[0] = 1 #since s[0] won't be 0, this situation is already crossed out in edge case 

        for i in xrange(1, len(dp)):
            if s[i] == '0' and (s[i-1] not in '12'): #single '0' can not be decoded, if s[i-1] is not 1, 2, thus the whole string is not valid     
                break;
            if s[i] != '0': #single 0 can not be decoded
                dp[i] += dp[i-1]
            if int(s[i-1:i+1]) < 27 and s[i-1] != '0': #if s[i-1: i-2) can be decoded 
                dp[i] += dp[i-2] if i >= 2 else 1


        return dp[-1]


"""
test
myTest = Solution()

#testcase 1):
print "----------------------------"
print "tc1: s='0'  ==> 0"
print myTest.numDecodings('0')

#testcase 2):
print "----------------------------"
print "tc2: s='010'  ==> 0"
print myTest.numDecodings('010')

#testcase 3):
print "----------------------------"
print "tc3: s='10'  ==> 1"
print myTest.numDecodings('10')

#testcase 4):
print "----------------------------"
print "tc4: s='100'  ==> 0"
print myTest.numDecodings('100')

#testcase 5):
print "----------------------------"
print "tc5: s='30'  ==> 0"
print myTest.numDecodings('30')

#testcase 6):
print "----------------------------"
print "tc6: s='123'  ==> 3"
print myTest.numDecodings('123')

#testcase 7):
print "----------------------------"
print "tc7: s='122122'  ==> 13"
print myTest.numDecodings('122122')

#testcase 8):
print "----------------------------"
print "tc8: s='12230122'  ==> 0"
print myTest.numDecodings('12230122')

#testcase 9):
print "----------------------------"
print "tc9: s='12212226923'  ==> 68"

#testcase 10):
print "----------------------------"
print "tc10: s='1011'  ==> 2"
print myTest.numDecodings('1011')
"""


