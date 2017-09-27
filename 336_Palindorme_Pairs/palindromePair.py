#check if a string is palindrome string
# @param s: string
# @return type: bool
def isPalindrome(s):

    #two pointers
    forw, back  = 0, len(s) - 1

    while forw <= back:
        if s[forw] != s[back]:
            return False
        forw += 1
        back -= 1

    return True

"""
Solution:
For word[i] and word[j], suppose length of word[i] is no larger than length of word[j] 
1). if reverse string of word[i] is prefix of word[j], and the rest of word[j] is a palindrome itself, then word[j] + word[i] is a palindrome string.
ex. word[i] = 'ba', word[j] = 'abcec', then word[j] + word[i] = 'abcecba'
2). if reverse string of word[i] is postfix of word[j], and the rest of word[j] is a palindrome itself, then word[i] + word[j] is a palindrome string.
ex. word[i] = 'lls', word[j] = 'sssll', then word[i]+word[j] = 'llssssll'
3). if word[i] and word[j] are same length, and reversed word[i] is equal to word[j], which means it is both prefix and postfix, then both word[i]+word[j] and word[j]+word[i] are palindrome string

Thus, for each word, check if it is a prefix/postfix of every other words.
Time complexity: if the average length of each word is w, then the time complexity will be O(wn^2). w is the time to compare between two strings in each loop
"""
class Solution2(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        
        res = []
        
        for i in xrange(len(words)):
            for j in xrange(i+1, len(words)):
                len_i = len(words[i])
                len_j = len(words[j])
                
                if len_i == len_j and words[i][::-1] == words[j]:
                    res += [ [i, j], [j, i]]
                    
                elif len_i < len_j:
                    r_word_i = words[i][::-1]
                    if r_word_i == words[j][: len_i] and self.isPalindrome(words[j][len_i:]): #prefix
                        res += [[j, i]]
                    if r_word_i == words[j][len_j - len_i:] and self.isPalindrome(words[j][:len_j-len_i]): #postfix
                        res += [[i, j]]
                        
                elif len_i > len_j:
                    r_word_j = words[j][::-1]
                    if r_word_j == words[i][: len_j] and self.isPalindrome(words[i][len_j:]): # word[j] is prefix
                        res += [[i, j]]
                    if r_word_j == words[i][len_i - len_j :] and self.isPalindrome(words[i][:len_i-len_j]): #postfix
                        res += [[j, i]]
                        
        return res

    #check if a string is palindrome string
    # @param s: string
    # @return type: bool
    def isPalindrome(self, s):
        
        #two pointers
        forw, back  = 0, len(s) - 1
        
        while forw <= back:
            if s[forw] != s[back]:
                return False
            forw += 1
            back -= 1
        
        return True

"""
Solution: (Time limit exceeds)
To reduce time complexity for above solution, use Trie to search for prefix and postfix.

Time complexity: O(wn)
If the average length for each word is w,  n is total number of words
O(wn) time to construst the Trie
O(w) time to search prefix and postfix in the Trie for each word
"""
#single Trie node class definition
class TrieNode(object):
    def __init__(self, x):
        self.val = x
        #to denote if the node is a leaf node or not
        self.leaf = False     
        
        # the state of current prefix till curren node is reversed string in words or not and its corresponding index in words
        # for the convenience of finding
        #(isreversed, index), ex. (1, 3)
        self.stateInWord = [] 
        
        self.children = [None] * 26
    
#Trie class definition
class Trie(object):
    def __init__(self):
        self.root = TrieNode('/')
    
    # insert one word in Trie
    # @param word    : string
    # @param reversed: bool, if the word is a reversed one in original words list
    # @param index    : int, index of this word in words list
    def insert(self, word, reversed, index):
        cur = self.root
        
        i = 0
        while i < len(word):
            ind = ord(word[i]) - 97
            
            if cur.children[ind] == None: #this char node does not exist in Trie
                #create a new node
                cur.children[ind] = TrieNode(word[i])
                
            cur.stateInWord += [(reversed, index)]
            cur = cur.children[ind]
            
            i += 1
        
        #update leaf node
        cur.leaf =  True
        cur.stateInWord += [(reversed, index)]
    
            
    # find if word is a prefix in Trie
    # @param word: string
    # @return type: []
    def search(self, word):
        
        cur = self.root
        i = 0
        while i < len(word):
            ind = ord(word[i]) - 97
            
            if cur.children[ind] != None:
                cur = cur.children[ind]
            else: #the word is not a prefix in the Trie
                return []
            i += 1
        
        return cur.stateInWord
            
        
    
class Solution1(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        
        res = []
        
        #pre calculate the reversed string of each word
        #save time for recalculating same reversed string
        rwords = [ w[::-1] for w in words]
        
        #construct Trie
        trie = Trie()
        for i, w in enumerate(words):
            trie.insert(w, 0, i)
            #trie.insert(w[::-1], 1, i)
            trie.insert(rwords[i], 1, i)
        
        #for w in words:
        #    print "searching ", w
        #    print trie.search(w)
        
        for i, w in enumerate(words):
            l = len(w)
            
            #tup = trie.search(w[::-1])
            tup = trie.search(rwords[i])
            for rev, ind in filter(lambda x: x[1] != i, tup):
                if rev == 0 and self.isPalindrome(words[ind][l:]): #reversed words[i] is words[ind]'s prefix, and the rest of words[ind] is palindrome     
                    res += [[ind, i]] if [ind,i] not in res else []
                    
            tup = trie.search(w)
            for rev, ind in filter(lambda x: x[1] != i, tup):
                if rev == 1 and self.isPalindrome(words[ind][:len(words[ind])-l]): #reversed words[i] is words[ind]'s postfix, and the rest of words[ind] is palindrome
                    res += [[i, ind]] if [i,ind] not in res else []
        
        return res
                        
            
            
    
"""
Solution:
This version of solution is the reversed thinking process of above ones.
In above ones, for each word wi, we find if it is a prefix or suffix of other word wj; and if the rest part of that wj is palindrome, they will be valid pair.
In current solution, for each word wi, we find all its prefixes and suffixes, if they are palindrome and the rest part of wi exists in words as another word wj, they can be valid pair.
Ex. ['cecab', 'ba', 'bacec'] 
prefix of 'cecab' => ['', 'c', 'ce', 'cec', 'ceca', 'cecab'] 
'' and 'cec' are palindromes, and it reversed of the rest 'bacec' and 'ba' are in words list. Thus, 'bacec' + 'cecab' and 'ba' + 'cecab' are valid pairs.

Ex. [ 'abcec', 'ba', 'cecba']
suffix of 'abcec' => ['', 'c', 'ce', 'cec', 'ceca', 'cecab']
'' and 'cec' are palindromes, and it reversed of the rest 'bacec' and 'ba' are in words list. Thus, 'abcec' + 'ba' and 'abcec' + 'cecab' are valid pairs.

We can hashtable to speed up looking for wj.
 
Time complexity: O(wn), w is the average length of word; n is the total number of words
"""
class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        
        res = []
        
        #construct hashmap { reversed word: index}
        hashmap = {}
        for i, w in enumerate(words):
            hashmap[w[::-1]] = i
        
        #iterating through words
        for i, w in enumerate(words):
            
            #print "new word ", w
            #find all prefixes and suffixes
            for j in xrange(len(w)+1):
                pref = w[:j]
                suff = w[j:]
                
                #print "pref, suff: ", pref, suff
                if isPalindrome(pref) and suff in hashmap and hashmap[suff] != i:
                    #print "bk1"
                    res += [[hashmap[suff], i]] 
                
                #Note that when considering suffixes, we explicitly leave out the empty string to avoid counting duplicates.
                #That is, if a palindrome can be created by appending an entire other word to the current word, 
                #then we will already consider such a palindrome when considering the empty string as prefix for the other word.
                if j != n and isPalindrome(suff) and pref in hashmap and hashmap[pref] != i:
                    #print "bk2"
                    res += [[i, hashmap[pref]]]
                    
        return res
                
                
                
            
"""
test
"""
myTest = Solution()
#print myTest.isPalindrome("a")
#print myTest.isPalindrome("aa")
#print myTest.isPalindrome("ab")
#print myTest.isPalindrome("aba")
#print myTest.isPalindrome("cabac")
#print myTest.palindromePairs(["abcd", "dcba", "lls", "s", "sssll"])
print myTest.palindromePairs(["ab","ba","abc","cba"])
