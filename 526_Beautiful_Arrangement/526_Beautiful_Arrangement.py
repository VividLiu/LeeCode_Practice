"""
second optimization:
No pre calculation and hash needed. Only count the number arrangements rather than output the actual arrangement.
Use backtracking algorithm, pick any possible value for current i position, then recursively try (i-1) position until it ends with valid arrangement or terminate before with no valid value to place at i' position.
Go downwards from N to 1, since lower numbers have more opitons (ex. 1 can go anyware). Thus, place the higher number first will have lower chance to end up with dead ends. Make it more effient. 
"""
class Solution(object):
    def countArrangement(self, N):
        """ 
        :type N: int
        :rtype: int
        """
        return self.count(N, set(range(1, N+1)))

    #recursive helper function
    #output 1 if current branch contributes to one valid solution
    #output 0 ( sum([]) ==> 0 ) if it terminates
    def count(self, i, setX):
        if i == 1:
            return 1
        return sum( self.count(i-1, setX - {x}) for x in setX if x % i == 0 or i % x == 0)
"""
First trial:
Pre calculate all valid values for each position and store this inform in hash. Then use backtracking algorithm to output all possible arrangements. 
"""

class Solution_2(object):
    
    def countArrangement(self, N): 
        """
        :type N: int
        :rtype: int
        """

        dict = self.findAllPosible(N)

        allArrange = []
        self.findArrange(N, [], allArrange, dict)

        return len(allArrange)
    
    # For each ith position, find all the posible values that could be placed at ith position.
    # Store the information in hash and return
    def findAllPosible(self, N): 
        """
        :type N:int
        :rtype: dictionary
        """
        dict = {}

        for i in xrange(1, N+1):
            dict[i] = reduce(list.__add__, ([j] for j in xrange(1, N+1) if i % j == 0 or j % i == 0))

        return dict

    #recursive function to find beautiful arrangement
    def findArrange(self, N, arrange, resSet, dict):
        """
        :N: type (int) 
        :arrange: type list, one possible arrangement so far 
        :resSet:  type list(list), all valid beautiful arrangements
        """
        #termination case
        #debugging
        #print "--------------------"
        #print "current arrange:"
        #print arrange

        if N == len(arrange):
            #find one valid arrangement
            #append it into the final result set
            resSet.append(arrange)
            return

        #if len(arrange) < N
        #continue picking the posible values for the rest position
    
        #choose one posible value for current position if any exist and append to current arrange list
        i = len(arrange) + 1 #current ith position
        p = filter(lambda x: x not in arrange, dict[i]) #valid values for current ith position

        #debugging
        #print "current position " + str(i)
        #print "valid values for i "
        #print p   

        if p: # p is not empty list
            for v in p:
                newArrange = arrange + [v] 
                self.findArrange(N, newArrange, resSet, dict)
        else: #p is empty, thus this path is not valid
            return 
