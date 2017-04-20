"""
Method 1:
The most straight forward method. 
Use the matrix multiplication equation:
C[i][j] += A[i][k]*B[k][j]
Time complexity is O(na*n*nb)
"""
class Solution_1(object):
    _debug = 0
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """

        if len(A) == 0 or len(B) == 0:
            return []

        #get the dimenstion
        na, n, nb = len(A), len(A[0]), len(B[0])

        if self._debug:
            print "the dimension of A is " + str(na) + "x" + str(n)
            print "the dimension of B is " + str(n) + "x" + str(nb)
    
        #initialize the return matrix
        C = [[ 0 for i in xrange(nb)] for j in xrange(na)]

        if self._debug:
            print "initialized C matrix is: "
            print C
    
        for i in xrange(na):
            for j in xrange(nb): 
                for k in xrange(n):
                    C[i][j] += A[i][k]*B[k][j]

        return C

"""
Method 1 optimization:
Since it is a sparse matrix, there are many zero elements in both A & B matrices.
In method 1, even A[i][k] is 0, we still multiply it nb times. To optimize the time
complexity, we change the order of for loops, so that loop through i, k first, 
if A[i][k] is not zero, we loop through j and do the calculation A[i][k]*B[k][j]
"""
class Solution_2(object):
    _debug = 0
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(A) == 0 or len(B) == 0:
            return []

        #get the matrices dimensition
        na, n, nb = len(A), len(A[0]), len(B[0])
        
        #initialize result matrix
        C = [ [0 for x in xrange(nb)] for x in xrange(na)]

        for i in xrange(na):
            for k in xrange(n):
                if A[i][k] != 0:
                    for j in xrange(nb):
                        C[i][j] += A[i][k] * B[k][j] 

        return C
        
"""
Method 2:
Since both A and B are sparse matrix, but they are stored in dense matrix format,
we can optimize the list(list(int)) data structure to reduce the time complexity.
Use hash table { i: { j: 1, j': 2}, i': { j:3, j':5}}
(i, j) is matrix index. htable[i] is the hash table of column indices of all nonzero elements.
"""
class Solution(object):
    _debug = 0
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """

        if len(A) == 0 or len(B) == 0:
            return []

        #get A, B dimention
        na, n, nb = len(A), len(A[0]), len(B[0])

        #initialize return matrix C
        C = [[ 0 for x in xrange(nb)] for x in xrange(na)]
        
        #hash table for matrix A, B
        hash_a, hash_b = {}, {}

        #preprocess A to get hash_A data stucture to represent A sparse matrix
        for i in xrange(na):
            for j in xrange(n):
                if A[i][j]: #nonzero element, store it in hash, with index as its key
                    #use dict.setdefault to create a new {} if hash_a[i] does not exist yet
                    hash_a.setdefault(i,{})[j] = A[i][j]

        """
        #one hash is enough
        #preprocess B to get hash_B data stucture to represent B sparse matrix
        for i in xrange(n):
            for j in xrange(nb):
                if B[i][j]: #nonzero elemnt, store it in hash
                    #use dict.setdefault to create a new {} if hash_b[i] does not exist yet
                    hash_b.setdafult(i,{})[j] = B[i][j]
        """

        #mulitplication
        for i in xrange(na):
            if i in hash_a: #if A[i] row has anything nonzero elements
                for k in xrange(n):
                    if k in hash_a[i]: #if A[i][k] is nonzero
                        for j in xrange(nb): #do all the caluculation that A[i][k] involves
                            C[i][j] += hash_a[i][k] * B[k][j]

        return C
            

"""
test
"""
myTest = Solution()

#testcase 1)
print "---------------------------------------"
print "tc1: A = [ ], B = [[2], [3]] => C = []" 
print myTest.multiply([], [[2],[3]])

#testcase 2)
print "---------------------------------------"
print "tc2: A = [ [2], [3] ], B = [] => C = []" 
print myTest.multiply([[2],[3]], [])

#testcase 3)
print "---------------------------------------"
print "tc3: A = [ [1,2]], B = [[2], [3]] => C = [[8]]" 
print myTest.multiply([[1,2]], [[2],[3]])

#testcase 4)
print "---------------------------------------"
print "tc4: A = [[1,0,0],[-1,0,3]], B = [[7,0,0],[0,0,0],[0,0,1]] => C = [[7,0,0],[-7,0,3]]" 
print myTest.multiply([[1,0,0],[-1,0,3]], [[7,0,0],[0,0,0],[0,0,1]])

#testcase 5)
print "---------------------------------------"
print "tc5: A = [ [1,-5]], B = [[12], [-1]] => C = [[17]]" 
print myTest.multiply([[1,-5]], [[12],[-1]])

