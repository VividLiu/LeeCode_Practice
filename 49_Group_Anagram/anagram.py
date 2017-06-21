"""
Solution:
Use hash table.
For each string in strs, sort the string using alphabetic order and use it as key.
"""
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = []
        hashTable = {} 
        
        for s in strs:
            key = list(s) 
            key.sort() #sort in alphabetic ascending order
            key = "".join(key) #join the list back to a string
            hashTable.setdefault(key, []).append(s)
        
        for key in hashTable:
            res.append(hashTable[key])
        
        return res

"""
test
"""
myTest = Solution()
print myTest.groupAnagrams(["eat","tea","tan","ate","nat","bat", "", "bat"])
