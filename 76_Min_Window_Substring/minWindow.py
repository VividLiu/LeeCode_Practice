from collections import deque
from collections import Counter

#Use hash table
#sudo code: 
#for i, c in enumerate(s):
#    if c in t:
#        cntTable[c] += 1 #how many times c exist in t 
#        indTable[c].append(i) #all index of c apperance in s 
#        
#        if flag: #indTable already contains window, update index
#            indTable[c].pop(0)
#
#        #the hashTable contains a window from now
#        if flag or all( cntTable[k] == len(indTable[k]) for k in indTable):
#            flag = True 
#            min = minimal value in hash
#            max = maximum value in hash
#            windows.append([min, max])
#
#if any( contTable[k] != len(indTable[k]) for k in indTable):
#    #no such window exist
#    return ""

#time complexity: O(S*T), S is the length of s, T is the lenth of t
class Solution2(object):
    _debug = 1
    
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        #sanity check:
        if len(s) == 0 or len(t) == 0:
            return ""
        
        win_s = -1            #minimal window start index in s
        win_e = -1            #minimal window end index in s
        minSize = len(s) + 1  #size of minimal window
        
        #initialize hashTable to record times of apperance of char c in t
        cntTable = {}
        #equavelent way to set default 
        #cntTable = defaultdict(int)
        for c in t:
            cntTable[c] = cntTable.setdefault(c, 0) + 1 
        
        #initialize hashtable to record current window index
        indTable = {}
        
        #boolean variable to signal that the indTable contains a window
        flag = False
        
        for i, c in enumerate(s, 1):
            if c in t:
                #use deque() instead of list, thus popleft only takes O(1) time
                indTable.setdefault(c,deque()).append(i)
                
                #only keep the lastest index
                if len(indTable[c]) > cntTable[c]:
                    indTable[c].popleft()
                    
                #contains all characters in t
                if flag or all( (k in indTable) and (cntTable[k] == len(indTable[k])) for k in cntTable): 
                    flag = True
                        
                    min_ind = min(indTable[k][0] for k in indTable)
                    max_ind = max(indTable[k][-1] for k in indTable)
                    
                    if max_ind - min_ind + 1 < minSize:
                        win_s = min_ind
                        win_e = max_ind
                        minSize = max_ind - min_ind + 1
                
                if self._debug:
                    print "indTable ", indTable
                    
        if self._debug:
            print "cntTable: ", cntTable
        
        if minSize == len(s) + 1:
            return ""
        else:
            return s[win_s : win_e+1]

#Solution:
#Use hashtable and two pointers, the slower pointer i marks the start of the window, the faster pinter j marks the end of the window. Thus, the size of the current window is j-i+1 
#The algorithm denotes on how to move the i, j pointer in O(n) time complexit  to cover all possible window or constrained substring
#In the iteration to advance j, we are trying to find a window with starting position at i'.
#Once we found j' which s[i':j'], j' inclusively, covers the all characters in string t. In other words, satisfied the substring constraint.
#We can start moving i to shrink the substring s[i': j']
#When moving i, if the substring is stilled valid, we can continue moving i, until the substring is not valid anymore; then, we can start moving j again to find another valid substring.
#time Complexity: O(n), n is the length of s

#For most substring problem, we are given a string and need to find a substring of it which satisfy some restrictions. A general way is to use a hashmap assisted with two pointers. 
class Solution(object):
    _debug = 1
    
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        #sanity check
        if len(s) == 0 or len(t) == 0:
            return ""
        
        #tMap is hash table with distinguished chars in t as keys, and  times of appearance in t for each char as value
        #use python module collections.Counter()
        #ex. Couter('ABCA') => {'A': 2, 'B': 1, 'C': 1}
        tMap = Counter(t)
        
        #counter denotes how many charactesr do we still need to form a window
        #it servers as a monitor, when counter == 0, we found a window
        counter = len(t)  
        
        #the slower and faster pointer
        #the slower pointer points to the start of current window
        #the faster pointer points to the end of current window
        i, j = 0, 0
        
        #win_i is the start index of minimal window
        #win_j is the end index of minimal window
        win_i, win_j = 0, 0
        
        #enumerate(s, n)
        #count, start with n, default start as 0
        for j, c in enumerate(s, 1):
            #tMap[c] > 0 means to form a window, we still need tMap[c] times character c
            #here, we found one at position j, thus, counter variable decrement one
            if (c in t) and tMap[c] > 0:
                counter -= 1
                
            #also need to update how many c are still needed 
            if c in t:
                tMap[c] -= 1
                
            #when a window is found, 
            #start advance i to shrink the window
            while counter == 0 and i < j:
                #record current window if it is smaller
                #not win_j <==> win_j == 0, which means win_j is never updated by now
                if not win_j or j - i < win_j - win_i:
                    win_j, win_i = j, i
                    
                if s[i] not in t:
                    i += 1
                else:
                    tMap[s[i]] += 1
                    #after we remove s[i] from curren window, 
                    #the window is not valid anymore
                    if tMap[s[i]] > 0:
                        counter += 1
                    i += 1
                        
        return s[win_i:win_j]
        
         
"""
myTest
"""
myTest = Solution()

#testcase 1): 
print "--------------------------------------"
print "tc1: s = 'ADOBECODEBANC', t= 'ABC' ==> 'BANC'"
print myTest.minWindow("ADOBECODEBANC", "ABC")

#testcase 2): 
print "--------------------------------------"
print "tc2: s = 'ADOABEFCODEBANC', t= 'ABC' ==> 'BANC'"
print myTest.minWindow("ADOABEFCODEBANC", "ABC")

#testcase 3): 
print "--------------------------------------"
print "tc3: s = 'AXXAXXCBXXDXXAXBXCXD', t= 'ABCD' ==> 'AXBXCXD'"
print myTest.minWindow("AXXAXXCBXXDXXAXBXCXD", "ABCD")

#testcase 4): 
print "--------------------------------------"
print "tc4: s = 'aa', t= 'aa' ==> 'aa'"
print myTest.minWindow("aa", "aa")

#testcase 5): 
print "--------------------------------------"
print "tc5: s = 'aaabc', t= 'de' ==> ''"
print myTest.minWindow("aaabc", "de")

#testcase 6): 
print "--------------------------------------"
print "tc5: s = 'a', t= 'a' ==> 'a'"
print myTest.minWindow("a", "a")
        
        
        
        
        
        
        
        
        
