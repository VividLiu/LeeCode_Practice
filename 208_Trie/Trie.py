"""
Time complexity analysis:
insert():   O(l), l is the length of word to be inserted
search():   O(l), l is the length of word to be searched
startsWith: O(l), l is the length of prefix to be searched
"""
class TrieNode(object):
    def __init__(self, key):
        self.key      = key
        self.isleaf   = False
        self.children = [None] * 27 #26 alphabetic character + one empty "" for "" word

class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        #initialize the root of Trie
        self._dict = TrieNode('/')       

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        #edge case
        if word == "": 
            self._dict.children[26] = TrieNode("") 
            self._dict.children[26].isleaf = True
    
    
        cur = self._dict
        for c in word:
            ind = ord(c) - 97
            if cur.children[ind] != None :
                cur = cur.children[ind]
            else:
                cur.children[ind] = TrieNode(c)
                cur = cur.children[ind]
        cur.isleaf = True
    

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        #edge case
        if word == "": 
            return True if self._dict.children[26] != None else False

        cur = self._dict
        for c in word:
            ind = ord(c) - 97
            if cur.children[ind] == None:
                return False
            cur = cur.children[ind]

        return True if cur.isleaf == True else False
    

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        cur = self._dict
        for c in prefix:
            ind = ord(c) - 97
            if cur.children[ind] == None:
                return False
            cur = cur.children[ind]

        return True 
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
