class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        #get the reversed strings
        rev_a = a[::-1]
        rev_b = b[::-1]

        #get length of a, b
        la, lb = len(a), len(b)

        #current digit of a, b
        #the result of current digit and carrier
        d1, d2, d, c = 0, 0, 0, 0

        #adding result in string
        r = ""

        #
        #for i in xrange( max(la, lb)):
        i = 0 
        while i < la or i < lb or c != 0:  
            d1 = int(rev_a[i]) if i < la else 0
            d2 = int(rev_b[i]) if i < lb else 0
    
            d, c = (d1+d2+c) % 2, (d1+d2+c)/2

            r += str(d)

            i += 1


        return r[::-1]
        
"""
test
myTest = Solution()

#testcase 1)
print "tc1: a = 11, b = 1"
print myTest.addBinary("11", "1")
#==> 100

#testcase 2)
print "tc2: a = 10, b = 1"
print myTest.addBinary("10", "1")
#==> 11

#testcase 3)
print "tc3: a = 0, b = 0"
print myTest.addBinary("0", "0")
#==> 0

#testcase 4)
print "tc4: a = 111, b = 111"
print myTest.addBinary("111", "111")
#==> 1110

#testcase 5)
print "tc5: a = 1, b = 11"
print myTest.addBinary("1", "11")
#==> 100
""" 


