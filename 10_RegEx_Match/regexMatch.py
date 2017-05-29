"""
Recursive
Exceeds time limit
"""
class Solution3(object):
    _debug = 0

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        return self.helper(s, p, 0, 0)

    #-------------------------------------------------------------------
    # matching substring s[i:], p[j:]
    #-------------------------------------------------------------------
    def helper(self, s, p, i, j):
        if self._debug:
            print "     matching " + s[i:] + ", " + p[j:] + " i= " + str(i) + "," + "j=" + str(j)

        if i == len(s) and j == len(p):#reaching end of both string, match succeed
            if self._debug:
                print "     matched"
            return True
        elif i == len(s) or j == len(p):#reaching one end, not matched
            if self._debug:
                print "     not matched"
            return False

        res = False

        # if next patten character is *, the current patten character can be skipped if
        # * takes value 0
        if j < len(p)-1 and p[j+1] == '*':
            res = self.helper(s, p, i, j+2) 

        #not reaching either end, matching in progress
        if p[j] == '*':
            if self._debug:
                print "             case '*'"     
            #get the preceding character
            if j > 0:
                c = p[j-1]  
            else: 
                return False #return false if the first character in pattern is '*' 
        
            k = i
            # '*' can match zero or more
            while k < len(s) and (s[k] == c or c == '.'):
                res = res | self.helper(s, p, k+1, j+1)
                k += 1 
            return res
        elif s[i] == p[j] or p[j] == '.':
            if self._debug:
                print "         case: s[i] == p[j]"
            res = res | self.helper(s, p, i+1, j+1)
        #elif p[j+1] == '*': #s[i] != p[j]
        #    if self._debug:
        #        print "         case: s[i] != p[j] but p[j+1] = '*'"
        #    res = res | self.helper(s, p, i, j+2)
        else:
            if self._debug:
                print "     not matched, case: rest"
            return False
        
        return res

"""
Dynamic programming
dp[i][j] = 1: p[0:i] (i inclusively) matches s[0:j] (j inclusively)
         = 0: p[0:i] does not match  s[0:j]
The condition to consider:
1) Need to take care empty string of s or p separatly
2) If pi is not * and pi can match sj (pi == sj or pi == '.')
    Then p[0:i] matches s[0:j], if
    - either, p[0:i-1] matches s[0:j-1]
    - or, p[0:k] matches s[0:j-1] where p[k+1:i-1] can be skipped using *
3) If pi is *
    If X* matches none,     p[i-1:i] is skipped, thus dp[i][j] = dp[i-2][j]
    If X* matches one,      * matches nothing, thus dp[i][j] = dp[i-1][j]
    If X* matches multiple, * matches one or more X character, thus dp[i][j] = dp[i][j-1] if p(i-1) matches sj

"""
class Solution2(object):
    _debug = 0

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        #special case, when s is empty string
        if s == "":
            if len(p) == 0:
                return True
            elif len(p) % 2 == 1: #even number
                return False
            else:
                i = 1
                for i in xrange(1, len(p), 2):#1,3,5...2n+1
                    if p[i] != '*':
                        return False
                return True

        #special case, when p is empty string
        if p == "":
            return False

        #initiate two dimensional dp array which is len(p) * len(s)
        dp = [ [ 0 for i in xrange(len(s))] for i in xrange(len(p))]

        if self._debug:
            print "initial dp array"
            print dp

        #fill the first row of dp array
        #dp[0][0] will be 1 which indicate p[0] matchs s[0] if they are either same characters or p[0] is '.' which matchs any character 
        #the rest elements in the first row will be 0 since p[0] can matchs s[0]
        if s[0] == p[0] or p[0] == '.':
            dp[0][0] = 1

        #fill the first column of dp array
        for i in xrange(1, len(p)):
            # if p[i] == s[0] and the sub pattern p[0:i-1] can be skipped, pi can match s0
            if (p[i] == s[0] or p[i] == '.'):
                j = i-1
                while j > 0 and p[j] == '*':
                    j = j - 2
                dp[i][0] = 1 if j < 0 else 0 #all p[0:i-1] can be skipped
            if p[i] == '*':
                k = i - 1
                #when * = 1 and no any p[0:l] matches s[0] l < k
                if (p[k] == s[0] or p[k] == '.') and (k == 0 or all(p[l] == '*' for l in xrange(k-1, -1, -2)) ):            
                    dp[i][0] = 1

                #when * = 0
                #if sum( [dp[l][0] for l in xrange(0,k)]) > 0:
                if k >= 1 and dp[k-1][0] == 1:
                    dp[i][0] = 1

        #fill the rest
        for i in xrange(1, len(p)):
            for j in xrange(1, len(s)):
                if self._debug:
                    print "---------------------------"
                    print "i, j: " + str(i) + ", "  + str(j)
                #when pi is not '*' and pi match sj 
                if p[i] != '*' and ( p[i] == s[j] or p[i] == '.'):
                    if dp[i-1][j-1] == 1: #p[0:j-1] matches s[0:i-1]
                        #print "i, j, dp[i][j] " + str(i) + "," + str(j) + "," + str(dp[i][j])
                        dp[i][j] = 1
                        #dp[i][j] = dp[i-1][j-1]

                        if self._debug:
                            print "case 1: pi matches sj and p(i-1) matches s(j-1)"
                    else: #if we can skip some sub patterns p[k+1:i-1] until some p[0:k], k < i-1 matches s[0:j-1]
                        k = i-1
                        while k > 0:
                            if p[k] == '*': #if p[k] is '*', p[k-1:k] can be skipped, thus, if p[0:k-2] can matches s[0:j-1], then dp[i][j] = 1
                                if k >= 2 and j >= 1 and dp[k-2][j-1] == 1: 
                                    dp[i][j] = 1 
                                    break
                                #else: continue search
                            else:# if p[k] is not '*', p[k-1:k] can not be skiped, thus dp[i][j] = 0 
                                break
                            k -= 2

                        if self._debug:
                            print "case 2: pi matches sj, and p(k-2) matches s(j-1), k = " + str(k)

                        #to do

                #when pi is '*'
                #when pi is '*'
                if p[i] == '*':
                    dp[i][j] = 1 if (dp[i-1][j-1] == 1 and (p[i-1] == s[j] or p[i-1] == '.')) or (dp[i][j-1] == 1 and (p[i-1] == s[j] or p[i-1]=='.'))  or (dp[i-1][j] == 1 and (p[i-1] == s[j] or p[i-1] == '.')) or dp[i-2][j] else 0
                    #dp[i][j] = dp[i-1][j-1] | dp[i][j-1] | dp[i-1][j]
                    #dp[i-2][j]  : when * = 0
                    #dp[i-1][j]  : when * = 1
                    #dp[i-1][j-1]: when * = 2
                    #dp[i][j-1]  : when * > 2

                    if self._debug:
                        print "case 3: pi is *"


        if self._debug:
            print "computed dp array"
            print dp

        if dp[-1][-1] == 1:
            return True
        else:
            return False

"""
Dynamic programming (simplified version)
Compared to my version of dynamic programming

dp[0][0]: if empty pattern matches empty string
dp[0][j]: p is empty pattern, to matches s
dp[i][0]: s is empty string
Thus, no need to take care empty string or pattern separately

dp[i][j] = 1: p[0:i-1] (i-1 inclusively) matches s[0:j-1] (j-1 inclusively)
         = 0: p[0:i-1] does not match  s[0:j-1]

The condition to consider:
1) If pi is not * and pi can match sj (pi == sj or pi == '.')
    Then p[0:i] matches s[0:j], if p[0:i-1] matches s[0:j-1]
2) If pi is *
    If X* matches none,     p[i-1:i] is skipped, thus dp[i][j] = dp[i-2][j]
    If X* matches one,      * matches nothing, thus dp[i][j] = dp[i-1][j]
    If X* matches multiple, * matches one or more X character, thus dp[i][j] = dp[i][j-1] if p(i-1) matches sj
"""
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype : bool
        """
        #initialize dp array
        dp = [ [ 0 ] * (len(s) + 1)  for _ in xrange(len(p) + 1) ]

        #fill the first row of dp array, which dp[0][j] denotes p is empty string
        dp[0][0] = 1

        #fill the first column of dp array, which dp[i][0] denotes s is empty string
        for i in xrange(1, len(p) + 1):
            dp[i][0] = dp[i-2][0] if (i>1 and p[i-1] == '*') else 0

        #fill rest
        for i in xrange(1, len(p) + 1):
            for j in xrange(1, len(s) + 1):
                if p[i-1] == s[j-1] or p[i-1] == '.':
                    dp[i][j] = dp[i-1][j-1]
                elif p[i-1] == '*':
                    dp[i][j] = dp[i-2][j] | dp[i-1][j] | (dp[i][j-1] and (p[i-2] == s[j-1] or p[i-2] == '.'))
                    #dp[i-2][j] when x* matches none
                    #dp[i-1][j] when x* matches one
                    #dp[i][j-1] when x* matches multiple times

        return True if dp[-1][-1] == 1 else False 
                

"""
test
"""
myTest = Solution()

print "--------------------------------------"
print "tc1: s = 'aa', p ='aa' ==> True"
print myTest.isMatch('aa', 'aa')

#testcase 2):
print "--------------------------------------"
print "tc2: s = 'aa', p ='a' ==> False"
print myTest.isMatch('aa', 'a')

#testcase 3): when '*' matchs zero
print "--------------------------------------"
print "tc3: s = 'a', p ='a*a' ==> True"
print myTest.isMatch('a', 'a*a')
        
#testcase 4): when '*' matchs one
print "--------------------------------------"
print "tc4: s = 'aaa', p ='a*a' ==> True"
print myTest.isMatch('aaa', 'a*a')

#testcase 5): when '*' can match different numbers
print "--------------------------------------"
print "tc5: s = 'aaaaa', p ='a*a*' ==> True"
print myTest.isMatch('aaaaa', 'a*a*')

#testcase 5): when '*' can match different numbers
print "--------------------------------------"
print "tc5: s = 'aab', p ='c*a*b* ==> True"
print myTest.isMatch('aab', 'c*a*b*')
#start introducting '.'
#testcase 6): 
print "--------------------------------------"
print "tc6: s = 'aa', p ='.*' ==> True"
print myTest.isMatch('aa', '.*')

#testcase 7): 
print "--------------------------------------"
print "tc7: s = 'ab', p ='.*' ==> True"
print myTest.isMatch('aa', '.*')

#testcase 8): 
print "--------------------------------------"
print "tc8: s = 'a', p ='.*' ==> True"
print myTest.isMatch('a', '.*')

#testcase 9): 
print "--------------------------------------"
print "tc9: s = 'a', p ='.*..a*' ==> False"
print myTest.isMatch('a', '.*..a*')

#testcase 10): 
print "--------------------------------------"
print "tc10: s = 'aaa', p ='ab*a*c*a' ==> True"
print myTest.isMatch('aaa', 'ab*a*c*a')

#testcase 11): 
print "--------------------------------------"
print "tc11: s = 'aaa', p ='b*a*c*a' ==> True"
print myTest.isMatch('aaa', 'b*a*c*a')

#testcase 12): 
print "--------------------------------------"
print "tc12: s = 'aaaaab', p ='a*a*b' ==> True"
print myTest.isMatch('aaaaab', 'a*a*b')

#testcase 13): 
print "--------------------------------------"
print "tc13: s = '', p ='a*' ==> True"
print myTest.isMatch('', 'a*')

#testcase 14): 
print "--------------------------------------"
print "tc14: s = '', p ='.*' ==> True"
print myTest.isMatch('', '.*')

#testcase 13): 
print "--------------------------------------"
print "tc15: s = '', p ='.*a' ==> False"
print myTest.isMatch('', '.*a')


#testcase 16): 
print "--------------------------------------"
print "tc16: s = 'aab', p ='b.*' ==> False"
print myTest.isMatch('aab', 'b.*')

#testcase 17): 
print "--------------------------------------"
print "tc16: s = 'caaaaccabcacbaac', p ='b*.*..*bba.*bc*a*bc' ==> False"
print myTest.isMatch('caaaaccabcacbaac', 'b*.*..*bba.*bc*a*bc')


