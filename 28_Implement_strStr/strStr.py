"""
Solution:
Iterate through haystack, if the first character of needle matches, compare needle with the follwing substring.
"""
class Solution2(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        #edge case
        if needle == "":
            return 0

        for i in xrange(len(haystack)-len(needle)+1):
            if haystack[i] == needle[0]:
                if needle == haystack[i:i+len(needle)]:
                    return i

        return -1

"""
Use KMP pattern searching algorithm.
For KMP reference: http://www.geeksforgeeks.org/searching-for-patterns-set-2-kmp-algorithm/
"""
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        #edge case:
        if needle == "":
            return 0

        #construct lps array
        lps = self.LPS(needle)

        i, j = 0, 0
        #for i in xrange(len(haystack) - len(needle) + 1):
        while i < len(haystack): 
            if haystack[i] == needle[j]:
                if j == len(needle)-1:
                    return i - len(needle) + 1
                i += 1
                j += 1
            else:
                if j == 0:
                    i += 1 
                else:
                    j = lps[j-1]
        return -1

    #construct array for longest proper prefix which is also suffix for pattern[0:i] 0 <= i < len(pattern)
    # @param pattern: str
    # @return param: List[int]
    def LPS(self, pat): 

        if pat == []:
            return []
    
        #initialize lps array
        #lps[0] is always 0, since the whole string is not a proper prefix
        lps = [0] * len(pat)

        #i is the prefix pointer, j is the suffix pointer
        i, j = 0, 1
        while j < len(pat):
            if pat[i] == pat[j]:
                i += 1
                lps[j] = i
                j += 1
            else:#pat[i] != pat[j]
                #note this is tricky.
                #. ex. aabaaac, when i = 2, which is 'b', and j = 5, which 'a'
                # pat[i] != pat[j], but we can't set lps[5] = 0, since pat[0:2) matches pat[4:6)
                if i != 0:
                    i -= 1
                else:
                    j += 1
        return lps

"""
test
"""
myTest = Solution()
print myTest.LPS("AABAACAABAA")
print myTest.LPS("aabaa")
print myTest.strStr("caabacacaabaaee", "aabaa")
print myTest.LPS("aabaaac")
print myTest.strStr("aabaaabaaac", "aabaaac")

            
             
                  

            
        

