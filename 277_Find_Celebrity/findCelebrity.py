# the knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
def knows(a, b):
    return True

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        #the candidates list that can be celebrity
        #(x, flag): n: person x, flag: = true if x has possibilty to be celebrity
        #the original set of candidates of celebrity is the full set of people before we cross out anyone
        candidates = []
        for i in xrange(n):
            candidates.append( [i, True])

        #print "initial candidates:"
        #print candidates
    
        #iterate through candidates to see if i is celebrity
        for i, tup in enumerate(candidates):
            if not tup[1]:
                continue
            for j in xrange(n):
                #print "i, j: " + str(i) + ", " + str(j)

                if i != j:
                    # if j knows i, j could not be celebrity, remove j from candidates
                    if knows(j, i): 
                        #remove j from candidates
                        candidates[j][1] = False
                            #print "     remove " + str(j)
    
                    else: #j doesn't know i, i couldn't be celebrity, break the outer loop
                        candidates[i][1] = False
                        #print "     remove " + str(i)
                        #reset j
                        j = 0 
                        break
    
                    #print "      new candidates:"
                    #print candidates
    
    
            if j == n-1: #everyone knows i, and make sure i doesn't know anyone
                #print "current i is celebrity"
                #print "j: " + str(j)
                res = False
                for k in xrange(n):
                    if k != i:
                        res |= knows(i, k)  
                if not res:
                    return i

    
        #print "final candidates"
        #print candidates
        return -1

"""
Solution:
Use an array to represent these n people p = [0, 1, 2, 3, 4, 5, 6...n-1]
Assume celebrity c = 0, iterate through the array and calls api knows(c, i), if c doesn't know i, i cannot be celebrity, continue the iteration until knows(c,i) return True or end of array, which means c does know i, then c can not be celebrity, set the current celebrity c = i and continue the iteration. This first iteration excludes anyone that cannot be celebrity. Then use another two iteration to check if c is really celebrity who knows noone but everyone knows him. 
Time complexity: O(n)
"""
class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        c = 0
        for i in xrange(1, n):
            if knows(c, i):
                c = i
        #check if c knows no one, since in the first iteration, know(c, j) j > c has already been called,
        #thus this iteration only needs to call j from 0 to c exclusivly
        for j in xrange(c):
            if knows(c, j):
                return -1

        #check if everyone knows c:
        for k in xrange(n):
            if not knows(k, c):
                return -1
        
        return c

"""
mytest
"""
myTest = Solution()
print myTest.findCelebrity(2)            





