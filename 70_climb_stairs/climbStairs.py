import numpy

class Solution(object):
    #2nd order square matrix multiplication function
    def matMultip(self, a, b):
        """
        :type a: 2nd-order numpy matrix
        :type b: 2nd-order numpy matrix
        :rtype: numpy matrix	
        """

        #return matrix initialization
        c = numpy.zeros((2,2))

        for i in xrange(2):
            for j in xrange(2):
                for k in xrange(2):
                    #debug
                    #print "single multip step"
                    #print "i = " + str(i) + ", j = " + str(j) +", k = " + str(k)
                
                    c[i,j] += a[i,k] * b[k,j]

        #debug
        print "in matMultip"
        print "a="
        print a
        print "b="
        print b
        print "multiplication result"
        print c
        print "-----------------------------"
        return c

    #2nd order square matrix square function
    def matSquare(self, a):
        """
        :type a: 2nd-order numpy matrix
        :rtype: numpy matrix	
        """
        #debug
        print "in matSquare"
        return self.matMultip(a,a)
                    
    #2nd order square matrix power function
    def matPower(self, a, n):
        """
        :type a: 2nd-order numpy matrix
        :type n: int
        :rtype: numpy matrix	
        """

        #debug
        #boundary case
        if n == 1:
            return a

        if n%2 == 0: #n is even
            subMat = self.matPower(a, n/2)
            
            #debug
            print "in matPower()"
            print "subMat for n=" + str(n/2)
            print subMat
            print "-------------------------"

            return self.matSquare(subMat)
        else: #n is odd
            subMat = self.matPower(a, (n-1)/2)

            #debug
            print "in matPower()"
            print "subMat for n=" + str((n-1)/2)
            print subMat
            print "-------------------------"

            return self.matMultip(self.matSquare(subMat), a) 

    # 
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        mat = numpy.matrix([[1,1],[1,0]])
        mat = self.matPower(mat, n)

        #debug
        print "final result matrix"
        print mat
        return mat[1,0]
    	

#testcase
myTest = Solution()
#print myTest.climbStairs(3);
print myTest.climbStairs(5);
#print myTest.climbStairs(5);






	
