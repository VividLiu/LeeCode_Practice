from collections import Counter

"""
This problem is similar to 76. Minimum window substring. The difference is that instead of finding a window, we will need to find a substring here. Thus no extra characters are allowd in the substring of s2.
Ex. s1='ab', s2 = 'xbaxacb'
    'ba' in s2 is the substring that is one of permutation of s1
    'acb' instead is a window that covers s1.
Use similar two pointer solution.
Whenever we hit some extra unwanted characters in the current searching substring, reset all counter and the search string to "" 
"""
class Solution(object):
    _debug = 0
    
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        
        #sanity check
        if len(s1) == 0:
            return True
        
        #initialize hash table counter which counts the times of appareance of each character in s1
        counter = Counter(s1)
        
        #variable to signal that all characters in s1 have been found in current searching substring
        flag = len(s1)
        
        i, j = 0, 0
        I, J = 0, 0
         
        for j, c in enumerate(s2):
            if c not in counter:
                #reset counter and flag
                counter = Counter(s1)
                flag = len(s1)
                # and move i to next index 
                i = j+1
            else:
                #hit one needed c 
                if counter[c] > 0:
                    counter[c] -= 1
                    flag -= 1
                     
                    if self._debug:
                        print "    hit one needed " + c
                        print "    current i, j:", i, j 
                        print "    current counter:", counter
                        print "    current flag:", flag
                    if flag == 0:
                        if self._debug:
                            I, J = i, j 
                            print "    substring: ", s2[I: J + 1]
                        
                        return True
                else: #counter[c] == 0, hit one extra c, move i until we can discard one c in current searching string
                    while s2[i] != c:
                        counter[s2[i]] += 1
                        flag += 1
                        i += 1
                        
                    i += 1
                    
                    if self._debug:
                        print "    hit one extra " + c
                        print "    current i, j:", i, j 
                        print "    current counter:", counter
                        print "    current flag:", flag
        
        return False
                
"""
test
"""
myTest = Solution()

#testcase 1
print "---------------------------------"
print "tc1: s1='', s2 = 'eidbaxxx' ==> True"
print myTest.checkInclusion('', 'eidbaxxx')

#testcase 2
print "---------------------------------"
print "tc2: s1='', s2 = '' ==> True"
print myTest.checkInclusion('', '')

#testcase 3
print "---------------------------------"
print "tc3: s1='ab', s2 = '' ==> False"
print myTest.checkInclusion('ab', '')

#testcase 4
print "---------------------------------"
print "tc4: s1='ab', s2 = 'eidbaxxx' ==> True"
print myTest.checkInclusion('ab', 'eidbaxxx')

#testcase 5
print "---------------------------------"
print "tc5: s1='abb', s2 = 'eidbabxxx' ==> True"
print myTest.checkInclusion('abb', 'eidbabxxx')

#testcase 6
print "---------------------------------"
print "tc6: s1='aab', s2 = 'aaaab' ==> True"
print myTest.checkInclusion('aab', 'aaaab')

#testcase 7
print "---------------------------------"
print "tc7: s1='caabd', s2 = 'caaaabdc' ==> True"
print myTest.checkInclusion('caabd', 'caaaabdc')

#testcase 8
print "---------------------------------"
print "tc8: s1='abc', s2 = 'aaaabd' ==> False"
print myTest.checkInclusion('abc', 'aaaabd')
            
                
            
        
