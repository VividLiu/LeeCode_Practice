""" 
    dynamic programming
"""
class Solution(object):
    def numberOfArithmeticSlices(self, A): 
        dp = [0] * len(A)

        for i in xrange(2, len(A)):
            if A[i] - A[i-1] == A[i-1] - A[i-2]:
                dp[i] = dp[i-1] + 1 

        return reduce(lambda x,y: x+y, dp, 0) #sum the dp list
        

"""
My trial
Explanation in question.txt
"""
class Solution2(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) < 3:
            return 0

        slices = [A[0], A[1]]
        dif = A[1] - A[0]
        r = 0

        for i in xrange(2, len(A)):
            if dif == A[i] - A[i-1]:
                slices.append(A[i])
            else: #encounter a different difference
                if len(slices) >= 3:
                    r += self.numOfArithSlices(slices)

                dif = A[i] - A[i-1]
                slices = [A[i-1], A[i]]

        if len(slices) >= 3:
            r += self.numOfArithSlices(slices)

        return r

    #helper function
    def numOfArithSlices(self, A):
        n = len(A)

        #n*(n+1)/2 is the # of all substrings of a length n array
        #(n-1) is the number of all substrings with length 2 in a length n array
        #n is the number of all substrings with length n in a length n array
        #substract the number of length 1 & 2 substrings because arithmetic array has minimal length of 3 
        return 0 if n < 3 else n*(n+1)/2 - (n-1) - n
