"""
Use Trie (or prefix tree) as data structure
Ex. words: neeta, need, rent, napa

            null
           /    \
          n      r
         / \     |
        e   a    e
        |   |    |
        e   p    n
       / \  |    |
      t   d a    t 
      | 
      a
      
Time complexity:
    addWord(): O(l) l is the length of the word
    search(): O(l) l is the length of the word
"""
class TrieNode(object):
    def __init__(self, val):
        self.end = 0         #flag to mark current node is end of one word if end == 1
        self.val = val        #character of current node
        self.children = [None] * 27   #the list of TrieNodes reference which are chidren of current node. 26 albatic character and one ''
        
    
class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        
        self._dict = TrieNode('/')
        

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        
        #add "" to dictionary
        if len(word) == 0:
            self._dict.children[26] = TrieNode('')
            self._dict.children[26].end = 1
        
        cur, i = self._dict, 0
        
        while i < len(word):
            ind = ord(word[i]) - 97
            if cur.children[ind]: #current character exist in prefix
                cur = cur.children[ind]
                i += 1
            else:
                #create a new node
                cur.children[ind] = TrieNode(word[i])
                cur = cur.children[ind]
                i += 1
        cur.end = 1
        
        return None
                
        

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        
        if len(word) == 0: #''
            if self._dict.children[26] and self._dict.children[26].end == 1:
                return True
            else:
                return False
            
        cur, i = self._dict, 0
        
        return self.iSearch(word, self._dict)
        
    def iSearch(self, word, cur):
        
        #ending case
        if len(word) == 1 and word[0] == '.':
            return True if any( (cur.children[i] != None and cur.children[i].end == 1) for i in xrange(26)) else False
        if len(word) == 1 and word[0] != '.':
            ind = ord(word[0]) - 97
            return True if cur.children[ind] != None and cur.children[ind].end == 1 else False
            
        if word[0] != '.':
            ind = ord(word[0]) - 97
            if cur.children[ind]:
                return self.iSearch(word[1:], cur.children[ind])
            else:
                return False
        else: #word[0] == '.'
            res = False
            for i in xrange(26):
                if cur.children[i]:
                    res |= self.iSearch(word[1:], cur.children[i])
            return res
        

# Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary()
obj.addWord("")
obj.addWord("bad")
obj.addWord("dad")
obj.addWord("bed")
obj.addWord("mad")
print obj.search("")
print obj.search(".ad")
print obj.search("bed")
print obj.search("b.d")
print obj.search("ba")

