"""
use xor (exclusive or) bit operation to find the different bits between two numbers
since xor will set different bits to 1
then use x & (x-1) formula to count 1
"""
class Solution(object):
    def hammingDistance(self, x, y):
        x = x ^ y
        
        #cnt: hamming distance cnt
        cnt = 0
            
        while(x): #while x is not 0
            x = x & (x-1) #use x&(x-1) to erase the rightmost one each time
            cnt += 1
            
        return cnt

"""
use xor (exclusive or) bit operation
and use build in count() function to count 1
"""
class Solution2(object): 
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        
        x = x ^ y
        return bin(x).count('1');
        
"""
The most straight forward method
Not using any bit operation, treat the two numbers as strings, 
and iterate throught them to count how many different bits they have.
"""        
class Solution3(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        x_bin = bin(x) #ex. x_bin: 0b1000
        y_bin = bin(y)
        
        #l: longer string, reversed
        #s: shorter string, reversed
        if (len(x_bin) >= len(y_bin)):
            l,s = x_bin[::-1], y_bin[::-1]
        else:
            l,s = y_bin[::-1], x_bin[::-1]
        
        #cnt: hamming distance
        cnt = 0
        
        for i in range(len(s)):
            #reach the end of the shorter string
            if s[i] == 'b':
                #calculate how many 1s are in the rest of the longer string
                for c in l[i:]:
                    if c == '1':
                        cnt += 1
                        
                return cnt
            
            if s[i] != l[i]:
                cnt += 1
