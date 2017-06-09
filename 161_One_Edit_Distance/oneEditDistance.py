class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        s_len, t_len = len(s), len(t)
        
        if abs(s_len - t_len) > 1:
            return False
        
        counter = 0 #the counter variable for different characters in S and T or extra character in either S or T
        if s_len == t_len:
            for i in xrange(s_len):
                #increment counter when hiting different counter
                counter += 1 if s[i] != t[i] else 0
        else: 
            si, ti = 0, 0
            while si < s_len and ti < t_len:
                if s[si] != t[ti]:
                    counter += 1
                    if s_len > t_len:
                        si += 1
                    else: #s_len < t_len:
                        ti += 1
                else:
                    si += 1
                    ti += 1
            
            #not both pointers are at the end
            if not (si == s_len and ti == t_len):
                counter += 1
        
        return False if counter != 1 else True

"""
test
"""
myTest = Solution()
print "---------------------"
print "tc1: s='', t=''"
print myTest.isOneEditDistance("", "")

print "---------------------"
print "tc2: s='a', t=''"
print myTest.isOneEditDistance("a", "")

print "---------------------"
print "tc3: s='a', t='b'"
print myTest.isOneEditDistance("a", "b")

print "---------------------"
print "tc4: s='a', t='ab'"
print myTest.isOneEditDistance("a", "ab")

print "---------------------"
print "tc5: s='acb', t='ab'"
print myTest.isOneEditDistance("acb", "ab")

print "---------------------"
print "tc6: s='acbd', t='ab'"
print myTest.isOneEditDistance("acbd", "ab")

print "---------------------"
print "tc6: s='caaaa', t='daabaa'"
print myTest.isOneEditDistance("caaaa", "daabaa")
                    
            
                
