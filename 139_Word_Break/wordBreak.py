"""
Solution (Time limit exceeds)
Use hash table and recursivley match.
Construct a hash table with first letter of each string in wordDict as key, and the string as value.
Ex. wordDict = ['leet', 'code', 'lee', 't', 'code']
the hash table will be:
hashtable = {
    'l': ['leet', 'lee'],
    'c': ['code', 'cod'],
    't': ['t'],
}
Then start with the first letter in s, ex s = 'leetcode'
check if the letter 'l' exists in hashtable, if the word list exists and some word matches the substring from the current start letter. In these example, both 'leet' and 'lee' match a substring in s start from letter 'l'.
Then recursively do the above step using next start letter which is the letter following the matched substing, which will be 'c' for 'leet' and 't' for 'lee' in this example.
If we can match whole string, then reutrn True
Time complexity: depend on the form of wodDict, the time complexity can vary a lot.
in each recursive call, if the list length for that start letter is l, and average length for string in that list is n', then the time comlexity in each recursive call is O(ln').
"""
class Solution2(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        
        #sanity check
        if len(s) == 0:
            return True
        if len(wordDict) == 0:
            return False
        
        #construct the hashtable which use the first letter of string in wordDict as key
        hashTable = {}
        for word in wordDict:
            #since wordDict contains non-empty string, no need to check if word is ""
            hashTable.setdefault(word[0], []).append(word) 
            
        #
        return self.helper(s, s[0], 0, hashTable)

    def helper(self, s, startLetter, startIndex, hashTable):
        """
        :rtype: int
        """
        
        #print "helper: startLetter=" + startLetter + " startIndex=" + str(startIndex)
        
        if startIndex >= len(s):
            print "error: index out of range"
        if startLetter not in hashTable:
            return False
        
        res = False
        for word in hashTable[startLetter]:
            endIndex = startIndex + len(word)
            if endIndex < len(s) and word == s[startIndex: endIndex]:
                res |= self.helper(s, s[endIndex], endIndex,  hashTable)
            elif endIndex == len(s) and word == s[startIndex: endIndex]:
                return True
                
        return res

"""
Dynamic programming
dp is a one dimentional array with length = n+1, n is the length of s
dp[0] = 1 to make the code consistent with the first letter
dp[i] represents if s[0:i-1] (i-1 inclusivley) can be segmented as words in wordDict. 
Then, dp[j] = 1 if there are some i, which i < j,
      and dp[i] == 1;
      and the substring s[i:j-1] (inclusively) in wordDict.

Time complexity: O(n^2*d), n is length of string, d is length of dictionary
One iteration for j and inner iteration to find such i for each j, the time complexity to find if substring exist in wordDict is len(wordDict)
"""
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        #initialize dp array
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        
        for j in xrange(1,len(s) + 1):
            for i in xrange(j):
                if dp[i] == 1 and s[i: j] in wordDict:
                    dp[j] = 1
        
        return True if dp[-1] == 1 else False
"""
test
"""

myTest = Solution()
#testcase 1:
print "----------------------------------"
print "tc1: s='leetcode', wordDict = ['leet', 'code']"
print myTest.wordBreak('leetcode', ['leet', 'code']) 

#testcase 2: multiple possible combination exist
print "----------------------------------"
print "tc2: s='leetcode', wordDict = ['leet', 'code', 'lee', 't', 'code']"
print myTest.wordBreak('leetcode', ['leet', 'code', 'lee', 't', 'code']) 

#testcase 3: 
print "----------------------------------"
print "tc3: s='leetcode', wordDict = ['lee', 'ode', , 't', 'cod']"
print myTest.wordBreak('leetcode', ['lee', 'ode', 't', 'cod']) 

#testcase 4:  one word in wordDict can be used multiple times
print "----------------------------------"
print "tc4: s='leelee', wordDict = ['lee']"
print myTest.wordBreak('leelee', ['lee']) 

#testcase 4:  one word in wordDict can be used multiple times
print "----------------------------------"
print "tc5: "
print myTest.wordBreak('acaaaaabbbdbcccdcdaadcdccacbcccabbbbcdaaaaaadb',["abbcbda","cbdaaa","b","dadaaad","dccbbbc","dccadd","ccbdbc","bbca","bacbcdd","a","bacb","cbc","adc","c","cbdbcad","cdbab","db","abbcdbd","bcb","bbdab","aa","bcadb","bacbcb","ca","dbdabdb","ccd","acbb","bdc","acbccd","d","cccdcda","dcbd","cbccacd","ac","cca","aaddc","dccac","ccdc","bbbbcda","ba","adbcadb","dca","abd","bdbb","ddadbad","badb","ab","aaaaa","acba","abbb"])
