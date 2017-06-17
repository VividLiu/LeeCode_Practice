class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        
        #sanity check
        if len(num1) == 0 or len(num2) == 0:
            return "0"
        
        #special case
        if num1 == "0" or num2 == "0":
            return "0"
        
        #maximum possible result length
        resArr = [0] * (len(num1) + len(num2) + 1)
        
        #reverse
        rnum1 = num1[::-1]
        rnum2 = num2[::-1]
        
        for i in xrange(len(num1)):
            for j in xrange(len(num2)):
                mul = int(rnum1[i]) * int(rnum2[j])
                resArr[i+j] += mul
        
        #each cell in resArr can be one or two digits, do the carrier a
        c = 0
        for i in xrange(len(resArr)):
            resArr[i] += c 
            c = resArr[i] / 10
            resArr[i] = resArr[i] % 10
        
        res = "".join(map(str, resArr))
        res = res.rstrip('0'); 
        return res[::-1]

"""
test
"""
myTest = Solution()
print myTest.multiply("99", "99")
print myTest.multiply("999", "999")
print myTest.multiply("999", "0")
print myTest.multiply("999", "1")
